install.packages("tidyverse")
install.packages("tidytext")

library("dplyr")
library("tidytext")
library("tidyverse")

# skip_empty_rows = true elimina las filas en blanco
# si fuera false las rellena con NA
pdf_cmf <- read_lines("C:\\Users\\panch\\Desktop\\python\\PRACTICA\\out_text.txt", skip_empty_rows = TRUE)

# largo del pdf
length(pdf_cmf)

#Convertimos el vector de caracteres en un dataframe con 
# las variables: nro línea y texto
pdf_df <- tibble(parrafo = seq_along(pdf_cmf),texto = pdf_cmf)

str(pdf_df)
view(pdf_df)

# tokenizar
pdf_pal <- pdf_df %>% unnest_tokens(palabra, texto)
head(pdf_pal, n=200)

# frecuencia absoluta
pdf_freq_abs <- pdf_pal %>% count(palabra, sort=TRUE)
head(pdf_freq_abs)

# frecuencia relativa
pdf_freq_rel <- pdf_pal %>% count(palabra, sort = TRUE) %>% mutate(relativa = n / sum(n))
head(pdf_freq_rel)                                                                                        

# limpiar palabras 
stopwords <- get_stopwords("es")
stopwords <- stopwords %>% rename(palabra = word)

# eliminan las palabras inutiles 
pdf_limp <- pdf_pal %>%
  anti_join(stopwords)

# reordena el df
pdf_filtrado <- pdf_limp %>% count(palabra, sort = T) %>%
  filter(n > 1) %>% mutate(palabra = reorder(palabra, n))

head(pdf_filtrado)


# frecuencia absoluta limpia
pdf_freq_abs <- pdf_limp %>% count(palabra, sort=TRUE)
head(pdf_freq_abs)

# frecuencia relativa limpia
pdf_freq_rel <- pdf_limp %>% count(palabra, sort = TRUE) %>% mutate(relativa = n / sum(n))
head(pdf_freq_rel)                                                                                        

# Se convierte todo el texto a minúsculas
palabra <- tolower(pdf_limp$palabra)

# Eliminación de páginas web (palabras que empiezan por "http." seguidas 
# de cualquier cosa que no sea un espacio)
palabra <- str_replace_all(palabra,"http\\S*", "")

# Eliminación de signos de puntuación
palabra <- str_replace_all(palabra,"[[:punct:]]", " ")

# Eliminación de números
palabra <- str_replace_all(palabra,"[[:digit:]]", " ")

# Eliminación de espacios en blanco múltiples
palabra <- str_replace_all(palabra,"[\\s]+", " ")

df <- as_tibble(palabra)
