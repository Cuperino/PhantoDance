extends Node

const file_path = "res://Timeline.rk"

func _ready():
	Rakugo.connect("say", self, "_on_say")
	Rakugo.connect("step", self, "_on_step")

	Rakugo.parse_and_execute_script(file_path)

func _on_say(character:Dictionary, text:String):
	prints("say", character.get("name", ""), text)
  
func _on_step():
	prints("Press 'Enter' to continue...")

func _process(delta):
	if Rakugo.is_waiting_step() and Input.is_action_just_pressed("ui_accept"):
		Rakugo.do_step()
