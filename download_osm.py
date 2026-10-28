# Run this once with internet access to save OSM roads and waterways locally.
import json,urllib.parse,urllib.request,time
from pathlib import Path
bbox=(19.7744444444,99.1252777778,20.1480555556,99.5730555556)
b=','.join(map(str,bbox))
query=f'[out:json][timeout:180];(way["highway"~"^(motorway|trunk|primary|secondary|tertiary|residential|unclassified|service|track|living_street)$"]({b});way["waterway"~"^(river|stream|canal|ditch)$"]({b}););out geom;'
urls=['https://overpass.kumi.systems/api/interpreter','https://overpass-api.de/api/interpreter']
err=None
for url in urls:
 try:
  print('กำลังดาวน์โหลดถนนและลำน้ำจาก',url)
  req=urllib.request.Request(url,data=urllib.parse.urlencode({'data':query}).encode(),headers={'User-Agent':'MaeAiLearningMap/1.0'})
  with urllib.request.urlopen(req,timeout=240) as resp: obj=json.load(resp)
  features=[]
  for e in obj.get('elements',[]):
   if e.get('type')!='way' or len(e.get('geometry',[]))<2:continue
   tags=e.get('tags',{});kind='river' if tags.get('waterway') else 'road'
   features.append({'type':'Feature','geometry':{'type':'LineString','coordinates':[[p['lon'],p['lat']] for p in e['geometry']]},'properties':{'kind':kind,'subtype':tags.get('waterway') or tags.get('highway'),'osm_id':e['id']}})
  file=Path(__file__).with_name('osm-roads-rivers.geojson')
  file.write_text(json.dumps({'type':'FeatureCollection','features':features},separators=(',',':')),encoding='utf-8')
  print('สำเร็จ',len(features),'เส้น ->',file);break
 except Exception as ex:err=ex;print('ลองแหล่งสำรอง:',ex);time.sleep(2)
else:raise SystemExit('ดาวน์โหลดไม่สำเร็จ: '+str(err))
