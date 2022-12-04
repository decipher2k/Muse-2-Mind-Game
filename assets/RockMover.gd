extends Spatial


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

func _process(delta):
	
	if get_tree().root.find_node("RockPython",true,false).ready==true:		
		var split=4.698/50.0
		var thl:VSlider=get_tree().root.find_node("Threshhold",true,false)
		get_tree().root.find_node("RockPython",true,false).threshholdlevel=float(thl.value)
		
		var pos=split*float(get_tree().root.find_node("RockPython",true,false).max)
		get_tree().root.find_node("rock",true,false).transform.origin.y =0.2+pos
	else: if get_tree().root.find_node("RockPython",true,false).error==true:		
		OS.alert('The Muse 2 is not connected.', 'Error')
		get_tree().quit()
	
