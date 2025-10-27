Feature: Buscar una película y validar el título y la calificación
    Scenario: Validar el título y la calificación de Inception
        Given el usuario está en el homepage de imdb.com
        When busca la pelicula "Inception"
        And selecciona el primer resultado de IMDb
        Then el titulo debe ser "Origen"
        Then la calificación debe ser 8,8