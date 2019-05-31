#Test Traveler
test_traveler =["Erin Wilkes", "Shanghai, China", ["historical site"]]

#List of Destinations
destinations =["Paris, France", "Shanghai, China", "Los Angeles, USA", "So Paulo, Brazil", "Cairo, Egypt"]

#List of Attractions
attractions =[[] for i in destinations]

#Function to return index of the destination  in the Destinations list
def get_destination_index(destination):
  return destinations.index(destination)

#Function to return the index of the destination of the traveler
def get_traveler_location(traveler):
  traveler_destination =traveler[1]
  traveler_destination_index =get_destination_index(traveler_destination)
  return traveler_destination_index

#Function to add attractions
def add_attraction(destination, attraction):
  try:
  	destination_index =get_destination_index(destination)
  except ValueError:
    return
  attractions_for_destination =attractions[destination_index]
  attractions_for_destination.append(attraction)
  return

add_attraction("Los Angeles, USA", ["Venice Beach", 'Beach'])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("So Paulo, Brazil", ["So Paulo Zoo", ["zoo"]])
add_attraction("So Paulo, Brazil", ["Ptio do Colgio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#Function to find attractions
def find_attractions(destination, interests):
  destination_index =get_destination_index(destination)
  #print("Destination Index: " +str(destination_index))
  attractions_in_city =attractions[destination_index]
  #print("Attractions in City: " +str(attractions_in_city))
  
  attractions_with_interest =[]
  #print(str(interests))
  
  for i in attractions_in_city:
    possible_attraction =i
    for attraction in i[1]:
      attraction_tags =attraction
      for interest in interests:
        if interest ==attraction_tags:
          attractions_with_interest.append(possible_attraction[0])

  return attractions_with_interest

#Function to print attractions for traveler
def get_attractions_for_traveler(traveler):
  traveler_destination =traveler[1]
  traveler_interests =traveler[2]
  
  traveler_attractions =find_attractions(traveler_destination, traveler_interests)
  
  interests_string = "Hi " +str(traveler[0]) +", we think you'll like these places around " +str(traveler_destination) +":"
  
  if len(traveler_attractions) ==1:
    for i in traveler_attractions:
      interests_string +=" the " +str(i)  
  else:
    for i in traveler_attractions:
      interests_string +=" the " +str(i) +","
  return interests_string

#la_arts =find_attractions("Los Angeles, USA", ["art"])
#print(la_arts)
smills_france =get_attractions_for_traveler(["Dereck Smill", "Paris, France", ['monument']])
print(smills_france)

#print(get_destination_index("Paris, France"))
#test_destination_index =get_traveler_location(test_traveler)
#print(test_destination_index)
#print(attractions)



