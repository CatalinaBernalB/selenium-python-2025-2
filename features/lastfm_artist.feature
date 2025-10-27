Feature: Buscar un artista y validar la fecha del último release
    Scenario: Validar la fecha del último lanzamiendo de Bruno Mars
        Given el usuario está en el homepage de last.fm
        When busca al artista "Bruno Mars"
        And selecciona el primer resultado
        Then la fecha del último release debe ser "3 October 2025"