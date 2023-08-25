import requests 
class Pokemon:
    #Constructor
    def __init__(self,pokemon_name):
        #Pokemon API
        response = requests.get(url="https://pokeapi.co/api/v2/pokemon/"+pokemon_name)
        response.raise_for_status()
        data = response.json()
        #Atributes
        self.pokemon_name = data["name"]
        self.type = data["types"]
        self.Doubledamage_from = data["types"]
        self.Doubledamage_to = data["types"]
        self.evolves_to = data["species"]
        self.hp = data["stats"]
        self.attack = data["stats"]
        self.defense = data["stats"]
        self.base_experience = data["base_experience"]
        self.abilities = data["abilities"]
        self.color = data["species"]
        self.picture = data["sprites"]["other"]["dream_world"]["front_default"]
        self.Halfdamage_from = data["types"]
    #Getters
    def get_pokemon_name(self):
        return self.pokemon_name
    
    def get_pokemon_picture(self):
        return self.picture
    
    def get_type(self):
        types = []
        type_names = []
        
        types = self.type
        for i in range(len(types)):
            type_names.append(types[i]["type"]["name"]) 
        return ', '.join(type_names)
    
    def get_evolves_to(self):
        # Declaring auxiliar lists
        species = []
        evolutions = []
        # Fetching species url
        species = self.evolves_to
        species_url = species["url"]
        # Fetching new API
        response = requests.get(url=species_url)
        response.raise_for_status()
        data = response.json()
        # Fetching evolution chain url
        evolution_chain_url = data["evolution_chain"]["url"]
        # Fetching new API
        response = requests.get(url=evolution_chain_url)
        response.raise_for_status()
        data = response.json()
        
        #species.append(data["chain"]["evolves_to"][0])
        evolutions.append(data["chain"]["evolves_to"][0]["species"]["name"])
        evolutions.append(data["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"])
        
        return ', '.join(evolutions)
    
    def get_hp(self):
        # Declaring auxiliar lists
        stats = []
        #Fetching hp
        stats = self.hp
        hp = stats[0]["base_stat"]
        return hp

    def get_attack(self):
        # Declaring auxiliar lists
        stats = []
        # Fetching attack
        stats = self.attack
        attack = stats[1]["base_stat"]
        return attack

    def get_defense(self):
        # Declaring auxiliar lists
        stats = []
        # Fetching defense
        stats = self.defense
        defense = stats[2]["base_stat"]
        return defense

    def get_base_experience(self):
        # Fetching base experience
        experience = self.base_experience
        return experience
    
    def get_Doubledamage_from(self):
        types = []
        elements = []
        
        types = self.Doubledamage_from
        # Fetching damage relations url 
        damage_relations_url = types[0]["type"]["url"]
        # Fetching API 
        response = requests.get(url=damage_relations_url)
        response.raise_for_status()
        data = response.json()
        # Extracting double damages from (list)
        double_damage_from = data["damage_relations"]["double_damage_from"]

        for i in range(len(double_damage_from)):
            elements.append(double_damage_from[i]["name"])
        return ', '.join(elements)

    def get_Doubledamage_to(self):
        types = []
        elements = []

        types = self.Doubledamage_to
        # Fetching damage relations url
        damage_relations_url = types[0]["type"]["url"]
        # Fetching API
        response = requests.get(url=damage_relations_url)
        response.raise_for_status()
        data = response.json()
        # Extracting double damages from (list)
        double_damage_to = data["damage_relations"]["double_damage_to"]

        for i in range(len(double_damage_to)):
            elements.append(double_damage_to[i]["name"])
        return ', '.join(elements)

    def get_abilities(self):
        # Declaring auxiliar lists
        names = []
        info = []
        aux = []
        # Fetching defense
        aux = self.abilities
        for i in range(len(aux)):
           abilities_name = (aux[i]["ability"]["name"]) 
           description_url= aux[i]["ability"]["url"]
           # Fetching new API
           response = requests.get(url=description_url)
           response.raise_for_status()
           data = response.json()
           description = ""
           for j in range(len(data["effect_entries"])):
               if (data["effect_entries"][j]["language"]["name"]=="en"):
                   description_name = (data["effect_entries"][j]["effect"]) 
           #abilities[abilities_name]= description    
           names.append(abilities_name)
           info.append(description_name)
        return [names,info]
        
    
    def get_color(self):
        
        color_url = self.color["url"]
        # Fetching new API
        response = requests.get(url=color_url)
        response.raise_for_status()
        data = response.json()
        
        color = data["color"]["name"]

        if (color == "blue"):
            body_background = "#19A7CE"
            body_text_color =  "#F1F6F9"
            sub_heading_background = "#00235B"
            sub_heading2_background = "#00235B"
            fa_solid = "#F1F6F9"
        elif (color == "green"):
            body_background = "#BFDB38"
            body_text_color = "#000000"
            sub_heading_background = "#1F8A70"
            sub_heading2_background = "#1F8A70"
            fa_solid = "#F1F6F9"

        elif (color == "yellow"):
            body_background = "#FFD966"
            body_text_color = "#000000"
            sub_heading_background = "#F2921D"
            sub_heading2_background = "#F2921D"
            fa_solid = "#F1F6F9"

        else:
            body_background = "#E21818"
            body_text_color = "#F1F6F9"
            sub_heading_background = "#820000"
            sub_heading2_background = "#820000"
            fa_solid = "#F1F6F9"

        return {"body_background":body_background,"body_text_color": body_text_color,"sub_heading_background": sub_heading_background,"sub_heading2_background": sub_heading2_background,"fa_solid":fa_solid }