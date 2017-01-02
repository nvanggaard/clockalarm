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
	entity_id: scene.wakeup
	device_home: device_tracker.phone_id

```

entity_id (required) should contain the scene you want to run on alarm time

device_home (optional) should contain the device, or group of devices which should be home, to execute the scene.


If no values are given for the optional fields it will take the default values written in the code snippet.



