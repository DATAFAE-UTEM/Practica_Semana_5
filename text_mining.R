install.packages("pdftools")
install.packages("wordcloud2")

library("wordcloud2")
library("pdftools")
library("tm")

# ruta donde tengo 100 pdf
my_dir = "C:\\Users\\panch\\Desktop\\python\\PDFs"

# se pasan los pdf a una lista 
files <- list.files(path = my_dir, pattern = "pdf$")
files 

# se crea un corpus 
setwd(my_dir)
corp <- Corpus(URISource(files, encoding = "latin1"),
               readerControl = list(reader = readPDF, language = "es-419"))

# numero de documentos 
ndocs <- length(corp)
ndocs

##============================================##
          # LIMPIEZA DEL CORPUS #
corp <- tm_map(corp, content_transformer(tolower))
corp <- tm_map(corp, content_transformer(removePunctuation))
corp <- tm_map(corp, content_transformer(removeNumbers))
corp <- tm_map(corp, removeWords, stopwords("spanish"))
corp <- tm_map(corp, stripWhitespace)

# Ignorar palabras extrañas
minTermFreq <- ceiling(ndocs*0.1)

# Ignorar palabras muy comunes
maxTermFreq <- floor(ndocs*0.5)

# SE COMVIERTE EL CORPUS EN UNA TABLA DE CONTINGENCIA
dtm <- DocumentTermMatrix(corp,
                          control = list(
                            language = "es-419",
                            wordLengths = c(4, 15), # palabras entre 4 y 15 caracteres
                            bounds = list(global = c(minTermFreq, maxTermFreq)) # se dejan fuera los min y max
                          ))

inspect(dtm)

# TABLA DE CONTINGENCIA CON PALABRAS QUE APARECEN EN UN 20% DE LOS PDFs
dtm2 <- removeSparseTerms(dtm, 0.8)
inspect(dtm2)

# PARA VER TODA LA TABLA Y NO SOLO LAS QUE MAS SE REPITEN
M <- as.matrix(dtm)
o <- order(sM <- colSums(M), decreasing = TRUE)
write.csv(M[,o], paste0(my_dir, "DTM.csv"), fileEncoding = "UTF-8")


# NUBE DE PALABRAS
mywords <- data.frame(words = names(sM), freq = as.numeric(sM))
mywords2 <- mywords[mywords$freq > 15,]
wordcloud2(mywords2, fontFamily = "serif", 
           backgroundColor = "white", shape = 'pentagon', size = 0.4)


# MATRIZ DE DISTANCIA ENTRE DOCUMENTOS (METODO DE AGRUPAMIENTO JERARQUICO)
distMatrix <- dist(M, method = "euclidean")
groups <- hclust(distMatrix, method = "ward.D")
plot(groups, main = "Dendograma de PDFs", cex=0.9, hang=-1, 
     xlab = "", ylab = "Altura")
rect.hclust(groups, k = 10, border="blue")

