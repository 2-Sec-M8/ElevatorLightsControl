# ElevatorLightsControl

Use v2.py

How to use?
```
strip = GoveeController()

# Reset
strip.turn_off()

# when starting the experience:
strip.trigger_solid()

# when going up (10s):
strip.trigger_elevator_up()

# After 10s, a.k.a stable on a floor
strip.trigger_solid()

# Repeat going up

# When the crash sound is started (6s after crash is triggered)
strip.trigger_breaking()

# During the fall (10s after previous)
strip.trigger_breaking()

# When reaching the bottom (3s after previous)
strip.turn_off()
```
