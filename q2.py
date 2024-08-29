
students = {
    "student1":{"name":"Adarsh","class":"10","height":160,"weight":55,"preferred_sport":"football"},
    "student2":{"name":"Mridul","class":"12","height":170,"weight":65,"preferred_sport":"cricket"},
    "student3":{"name":"Kanishak","class":"11","height":165,"weight":70,"preferred_sport":"javelin throw"}
}

def generate_diet_plan(weight):
    if weight<60:
        return "High protein diet"
    elif weight < 70:
        return "Balanced diet with moderate carbs"
    else:
        return "Low carb diet with high fiber"

def recommend_sport(height,weight):
    agility=height/weight
    if agility>2.5:
        return "Football"
    elif 2.0<agility<= 2.5:
        return "Cricket"
    elif 1.8 <agility<=2.0:
        return "Javelin throw"
    else:
        return "Chess"

for key, details in students.items():
    height=details["height"]
    weight=details["weight"]
    diet_plan=generate_diet_plan(weight)
    recommended_sport =recommend_sport(height, weight)
    students[key]["diet_plan"] = diet_plan
    students[key]["recommended_sport"] = recommended_sport

for student, details in students.items():
    print(f"Student: {details['name']}")
    print(f"Class: {details['class']}")
    print(f"Height: {details['height']} cm")
    print(f"Weight: {details['weight']} kg")
    print(f"Preferred Sport: {details['preferred_sport']}")
    print(f"Diet Plan: {details['diet_plan']}")
    print(f"Recommended Sport: {details['recommended_sport']}")
    print()
    






        
    
