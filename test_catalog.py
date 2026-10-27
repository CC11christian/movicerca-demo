import json, pathlib, unittest
from unittest.mock import patch
import update_catalog as u
class Tests(unittest.TestCase):
 def test_station_normalization_and_quality(self):
  features={'objectIds':list(range(120))}
  def mock_fetch(url,params):
   if params.get('returnIdsOnly')=='true':return features
   if '/0/' in url:
    names=['Talismán','Polanco','San Joaquín','Bellas Artes']
   else:names=['Avenida Talismán','Otra estación']
   return {'features':[{'geometry':{'x':-99.11,'y':19.46},'attributes':{'objectid':n,'nombre':names[n%len(names)],'linea':'7'}} for n in range(120)]}
  with patch.object(u,'fetch',side_effect=mock_fetch):
   items,count=u.download(0,'metro');self.assertEqual(len(items),120);self.assertEqual(count,120)
   self.assertEqual(items[0]['type'],'metro')
 def test_quality_rejects_empty(self):
  with patch.object(u,'fetch',return_value={'objectIds':[]}):
   with self.assertRaises(RuntimeError):u.download(0,'metro')
if __name__=='__main__':unittest.main()
