# clockalarm
### DEPRECATED 
This is no longer maintained 

#### A clockalarm for Home Assistant to turn on a scene

Copy the clockalarm.py into `homeassistantfolder/custom_components`

input_boolean.yaml and input_select.yaml into 'homeassistantfolder'

These should be included in you configuration file by:
```yaml
input_boolean: !include input_boolean.yaml
```
and
```yaml
input_select: !include input_select.yaml
```


After this the clock alarm componenet can be initialized by inserting:

```yaml
clockalarm:
    entity_id: scene.wakeup
    device_home: device_tracker.phone_id

```

entity_id (required) should contain the scene you want to run on alarm time

device_home (optional) should contain the device, or group of devices which should be home (if one device is home, it executes the event!), to execute the scene.


If no values are given for the optional fields it will take the default values written in the code snippet.

The input_boolean and input_selects might be grouped as following:

```yaml
Alarm:
  - input_select.wake_up_time
  - input_select.transition_time
  - input_boolean.monday
  - input_boolean.tuesday
  - input_boolean.wednesday
  - input_boolean.thursday
  - input_boolean.friday
  - input_boolean.saturday
  - input_boolean.sunday
```
After everything is set-up a panel like this should be shown:

![](http://i.imgur.com/NeUNBjD.png)

