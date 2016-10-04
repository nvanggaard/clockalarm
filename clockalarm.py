"""
 " ----------------------------------------------------------------------------
 " "THE BEER-WARE LICENSE" (Revision 42):
 " <nvanggaard@gmail.com> wrote this file.  As long as you retain this notice you
 " can do whatever you want with this stuff. If we meet some day, and you think
 " this stuff is worth it, you can buy me a beer in return.
 " ----------------------------------------------------------------------------
"""
import logging
import datetime
import homeassistant.core
from homeassistant.util import Throttle
from datetime import timedelta

log = logging.getLogger(__name__)

DOMAIN = 'clockalarm'
WEEKDAY = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=60)
MIN_TIME_BETWEEN_FORCED_UPDATES = timedelta(seconds=60)

CONF_ENTITY = 'entity_id'
CONF_BRIGHTNESS = 'brightness'
CONF_COLOR = 'color'
CONF_COLOR_TEMP = 'color_temp'

def setup(hass, config):
	ENTITY_ID = config[DOMAIN].get(CONF_ENTITY)
	if ENTITY_ID == None:
		log.error('No entity is given!')
	elif not isinstance(ENTITY_ID, str):
		log.error('entity_id has the wrong type! It should be of type string')
	else:
		log.info('entity_id: ' + str(ENTITY_ID))

	BRIGHTNESS = config[DOMAIN].get(CONF_BRIGHTNESS)
	if BRIGHTNESS == None:
		log.info('No brightness is given, default is used: 255')
		BRIGHTNESS = 255
	elif not isinstance(BRIGHTNESS, int):
		log.error('brightness has the wrong type! It should be of type int')
	else:
		log.info('Brightness is set to: ' + str(BRIGHTNESS))

	COLOR = config[DOMAIN].get(CONF_COLOR)
	if COLOR == None:
		log.info('No color is given, default value is used: [255, 200, 115]')
		COLOR = [255, 200, 115]
	elif not isinstance(COLOR, list):
		log.error('color has the wrong type! It should be of type list')
	else:
		log.info('Color is set to: ' + str(COLOR))
	
	COLOR_TEMP = config[DOMAIN].get(CONF_COLOR_TEMP)
	if COLOR_TEMP == None:
		log.info('No color temp is given, default value is used: 370')
		COLOR_TEMP = 370
	elif not isinstance(COLOR_TEMP, int):
		log.error('color_temp has the wrong type! It should be of type int')
	else:
		log.info('Color temp is set to: ' + str(COLOR_TEMP))
	
	@Throttle(MIN_TIME_BETWEEN_UPDATES, MIN_TIME_BETWEEN_FORCED_UPDATES)
	def update(call):
		wake_up_time = hass.states.get('input_select.wake_up_time').state
		transition_time = hass.states.get('input_select.transition_time').state
		transition_time = int(transition_time) * 60
		time_to_execute = (datetime.datetime.now() + datetime.timedelta(seconds=int(transition_time))).time().isoformat()[0:5]
		if hass.states.get('input_boolean.' + WEEKDAY[datetime.datetime.today().weekday()]).state == 'off':
			log.info('No alarm for today')
		elif wake_up_time == time_to_execute:
			hass.services.call('homeassistant', 'turn_on', {"entity_id": ENTITY_ID, "transition":transition_time, "brightness":BRIGHTNESS, "rgb_color":COLOR, "color_temp":COLOR_TEMP })

		return True
	hass.bus.listen(homeassistant.core.EVENT_TIME_CHANGED, update)
	return True
