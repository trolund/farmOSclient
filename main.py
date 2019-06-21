import farmOS

hostname = 'localhost:8888/farm-7.x-1.1/'
username = 'trolund'
password = 'kode123'

farm = farmOS.farmOS(hostname, username, password)
success = farm.authenticate()

# Get farm info
info = farm.info()

# Get all logs
logs = farm.log.get()
# Get harvest logs
harvests = farm.log.get({
  'type':'farm_harvest'
  })
# Get log number 37
log = farm.log.get(37)

# Get all assets
assets = farm.asset.get()
# Get all animal assets
animals = farm.log.get({
  'type':'animal'
  })

# Get all areas
areas = farm.area.get()
# Get field areas
fields = farm.area.get({
  'area_type':'field'
  })

# Get all terms
terms = farm.term.get()
# Get all terms from farm_crops vocabulary
crops = farm.term.get('farm_crops')


print(areas)
print(log)

print(crops)