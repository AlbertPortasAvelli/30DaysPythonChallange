### #xercices ###

# 1 - names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

nordic_countries = countries[:5]

es, ru = countries[5:7]

print("Nordic Countries:", nordic_countries)
print("Estonia:", es)
print("Russia:", ru)