import requests
from bs4 import BeautifulSoup
import webbrowser
from classpokeapi import Pokemon

pokemons = ["charizard", "bulbasaur", "butterfree", "wartortle"]

##MENU
print("********Pokedex**********")
for i in range(len(pokemons)):
    print(f"{i+1}.{pokemons[i]}")
print("*************************")
while True:
    try:
        choice=(int(input("Choose your pokemon: ")))
        selected_pokemon = Pokemon(pokemons[choice - 1])
        break
    except IndexError:
        print("Choose a number between 1-4")
    except ValueError:
        print("Enter a valid number")

#CONTENT OF HTML 

html = BeautifulSoup(f"""
<!DOCTYPE html>
<html>
    <head>
        
        <title>{selected_pokemon.get_pokemon_name()}</title>
        <!--Google fonts links------------------------------------------------------->
        <link href='https://fonts.googleapis.com/css?family=Barlow Condensed' rel='stylesheet'>
        <link type="text/css" rel="stylesheet" class="thrive-external-font"
            href="https://fonts.googleapis.com/css?family=Muli:400,800,700,500,600,300,200,900&amp;subset=latin&amp;display=swap">
         <!--Font awesome------------------------------------------------------------------------------>
        <script src="https://kit.fontawesome.com/295be4a184.js" crossorigin="anonymous"></script>
        
  
            <!--CSS Style sheets link--------------------------------------------------------->
        <link rel="stylesheet" href="../static/styles.css">
        <script src="https://unpkg.com/scrollreveal"></script>
       
        
    </head>
    <body style = "background-color: {selected_pokemon.get_color()["body_background"]}; color: {selected_pokemon.get_color()["body_text_color"]};">
        <!-- Name section ------------------------------------------------------------------------------>
        <section id="Pokemon_name_section">
            <div class="container-fluid">
                <h1 class="Pokemon_name">{selected_pokemon.get_pokemon_name()}</h1>
            </div>
        </section>

        <!-- Stats section ------------------------------------------------------------------------------>
        <section id="Pokemon_stats_section">
                <div class="Pokemon_picture_container">
                    <img class="Pokemon_picture" src="{selected_pokemon.get_pokemon_picture()}">
                </div>    

                <div class="Pokemon_stats_container" style = "color: {selected_pokemon.get_color()["body_text_color"]}">
                    <h2><i class=></i> HP : {selected_pokemon.get_hp()}</h2> 
                    <h2><i class=></i> Attack : {selected_pokemon.get_attack()}</h2>
                    <h2><i class=></i> Defense : {selected_pokemon.get_defense()}</h2>
                    <h2><i class=></i> Base experience : {selected_pokemon.get_base_experience()}</h2>
                </div>
                
        </section>
        
        <!-- Type section ------------------------------------------------------------------------------>
        <section id="Pokemon_type_section">
            <h2 id="Sub-heading3" style = "background-color: {selected_pokemon.get_color()["sub_heading_background"]};">Type</h2>
            <div class="Pokemon_type_container">
                    <h2>{selected_pokemon.get_type()}</h2>
                 
                </div>

        </section>
        
        <!-- Evolves section ------------------------------------------------------------------------------>
        <section id="Pokemon_evolve_section">
            <h2 id="Sub-heading4" style = "background-color: {selected_pokemon.get_color()["sub_heading_background"]};">Evolves to</h2>
            <div class="Pokemon_type_container">
                    <h2>{selected_pokemon.get_evolves_to()}</h2>
                 
                </div>

        </section>

        
        <!-- Damage section ------------------------------------------------------------------------------>
        <section id="Pokemon_damage_section">
            <h2 id="Sub-heading" style = "background-color: {selected_pokemon.get_color()["sub_heading_background"]};">Damage data</h2>
            <div class="Pokemon_to_container">
                <h2>Double damage from: </h2>
                <h2>{selected_pokemon.get_Doubledamage_from()}</h2>
        
            </div>

            <div class="Pokemon_from_container">
                <h2>Double damage to: </h2>
                <h2>{selected_pokemon.get_Doubledamage_to()}</h2>
            </div>


        </section>

        <!-- Abilities section ------------------------------------------------------------------------------>
        <section id="Pokemon_abilities_section">
            <h2 id="Sub-heading2" style = "background-color: {selected_pokemon.get_color()["sub_heading_background"]};">Pokemon abilities</h2>
            <div class="Pokemon_a1">
                <h2>{selected_pokemon.get_abilities()[0][0]}</h2>
                <h2>{selected_pokemon.get_abilities()[1][0]}</h2>
        
            </div>
            <div class="Pokemon_a2">
                <h2>{selected_pokemon.get_abilities()[0][1]}</h2>
                <h2>{selected_pokemon.get_abilities()[1][1]}</h2>
            </div>
        </section>
        
    </body>
</html>
""", "html.parser")

##CREATE HTML FILE OF THE SELECTED POKEMON
with open(f"{selected_pokemon.get_pokemon_name()}.html", "w") as f:
    f.write(str(html))
print(f"{selected_pokemon.get_pokemon_name()}.html created successfully")
   