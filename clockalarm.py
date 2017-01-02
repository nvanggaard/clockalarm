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
CONF_HOME = 'device_home'

def setup(hass, config):
	ENTITY_ID = config[DOMAIN].get(CONF_ENTITY)
	DEVICE_HOME = config[DOMAIN].get(CONF_HOME)
	if ENTITY_ID == None:
		log.error('No entity is given!')
	elif not isinstance(ENTITY_ID, str):
		log.error('entity_id has the wrong type! It should be of type string')
	else:
		log.info('entity_id: ' + str(ENTITY_ID))

	@Throttle(MIN_TIME_BETWEEN_UPDATES, MIN_TIME_BETWEEN_FORCED_UPDATES)
	def update(call):
		wake_up_time = hass.states.get('input_select.wake_up_time').state
		time_to_execute = (datetime.datetime.now() + datetime.timedelta(seconds=int(0))).time().isoformat()[0:5]
		if hass.states.get('input_boolean.' + WEEKDAY[datetime.datetime.today().weekday()]).state == 'off':
			log.info('No alarm for today')
		elif wake_up_time == time_to_execute:
			if DEVICE_HOME == None:
				hass.services.call('homeassistant', 'turn_on', {"entity_id": ENTITY_ID })
			elif hass.states.get(DEVICE_HOME).state == 'home':
				hass.services.call('homeassistant', 'turn_on', {"entity_id": ENTITY_ID })

		return True
	hass.bus.listen(homeassistant.core.EVENT_TIME_CHANGED, update)
	return True
