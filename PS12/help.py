def convdate(data,time):
  data = data.lower().split("-")
  if len(data[0]) == 1:
    date = "0"+data[0]
  else:
    date = data[0]
  month = data[1]
  year = data[2]
  if month =='jan':
    month = '01'
  elif month =='feb':
    month = '02'
  elif month =='mar':
    month = '03'
  elif month =='apr':
    month = '04'
  elif month =='may':
    month = '05'
  elif month =='jun':
    month = '06'
  elif month =='jul':
    month = '07'
  elif month =='aug':
    month = '08'
  elif month =='sep':
    month = '09'
  elif month =='oct':
    month = '10'
  elif month =='nov':
    month = '11'
  elif month =='dec':
    month = '12'
  fstring = f"{year}-{month}-{date} {time}"
  return(fstring)

data = "1-Jan-2021"
time = "23:23:56"

print(convdate(data,time))