import re
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
count = 0
cuenta = 0
fecha = []
personas = []
conteo = []
MesYAño =[]
ConteoMesYAño =[]

archivo = open("Chat de WhatsApp con Brazzers community.txt",encoding="utf8")
Lines = archivo.readlines()
for line in Lines:
  count+=1
  z = re.search("(\d+.\d+.\d{2}) \d+:\d{2} (?:a|p)\. m\. - (.\w+[ \w]*:)",line)
  if z:
    cuenta+=1
    fecha.append(z.group(1).replace('\xa0',''))
    FechaTemp=z.group(1).replace('\xa0','').split('/')
    MesAño = FechaTemp[1]+'/'+FechaTemp[2]
    nombreTemp = z.group(2).replace(':','').replace('Ale Inc Canadiense','Tiburcio').replace('Krlo 2','Karlangas').replace('Lil Vera 8','Lil Vera G ').replace('Lil Veeera','Lil Vera G ').replace('+502 3172 9965','Demy').replace('Kbin Culon','Kevin O Javier')
    if nombreTemp not in personas:
      personas.append(nombreTemp)
      conteo.append(1)
    else:
      index = personas.index(nombreTemp)
      conteo[index]=conteo[index]+1
    if MesAño not in MesYAño:
      MesYAño.append(MesAño)
      ConteoMesYAño.append(1)
    else:
      index = MesYAño.index(MesAño)
      ConteoMesYAño[index]=ConteoMesYAño[index]+1
fig1 = go.Figure(go.Scatter(
    mode = "lines+markers",
    y = ConteoMesYAño,
    x = MesYAño))
fig1.update_layout(title_text='Mensajes enviados por mes')
fig2 = px.pie(personas, values=conteo, names=personas)
fig2.update_layout(title_text='Cantidad de mensajes enviados por persona')
pio.write_html(fig1, file='index.html')
with open('index.html', 'a') as f:
    f.write(fig2.to_html(full_html=False, include_plotlyjs='cdn'))
