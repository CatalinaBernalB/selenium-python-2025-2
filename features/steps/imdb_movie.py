from behave import given, when, then
from pages.imdb_home_page import ImdbHomePage
from pages.imdb_results_page import ResultsPageImdb
from pages.imdb_movie_page import ImdbMoviePage
from selenium import webdriver

@given('el usuario está en el homepage de imdb.com')
def step_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.imdb.com/")
    context.imdb_home = ImdbHomePage(context.driver)

@when('busca la pelicula "{movie_name}"')
def step_search_movie(context, movie_name):
    context.imdb_home.search_movie(movie_name)
    context.imdb_results = ResultsPageImdb(context.driver)


@when('selecciona el primer resultado de IMDb')
def step_select_result(context):
    context.imdb_results.click_movie_link()
    context.imdb_movie = ImdbMoviePage(context.driver)

@then('el titulo debe ser "{expected_name}"')
def step_validate_movie_name(context, expected_name):
    obtained_data = context.imdb_movie.get_movie_title()
    assert obtained_data == expected_name, f"Los títulos no coinciden: se esperaba '{expected_name}', pero se obtuvo '{obtained_data}'"


@then('la calificación debe ser {expected_rating}')
def step_validate_movie_rating(context, expected_rating):
    obtained_data = context.imdb_movie.get_movie_rating()
    assert obtained_data == expected_rating, f"Los raitings no coinciden: se esperaba '{expected_rating}', pero se obtuvo '{obtained_data}'"


