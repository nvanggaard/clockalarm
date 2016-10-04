# clockalarm

####A clockalarm for Home Assistant to turn on your philips hue

Copy the clockalarm.py input 'homeassistantfolder/custom_componenets'

input_boolean.yaml and input_select.yaml into 'homeassistantfolder'

These should be included in you configuration file by:
```
input_boolean: !include input_boolean.yaml
```
and
```
input_select: !include input_select.yaml
```


After this the clock alarm componenet can be initialized by inserting:

```
clockalarm:
	entity_id: light.personal
	brightness: 255 
	color: [255 200 115] 
	color_temp: 370 
```

entity_id (required) should contain your light, or group of light.

brightness (optional) the value the light will get after transition

color: (optional) [red green blue] values for the color of the light

color_temp: (optional) color temperature

If no values are given for the optional fields it will take the default values written in the code snippet.

Into your configuration file, Brightness, color and color_temp are optional.


