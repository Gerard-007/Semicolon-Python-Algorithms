
def convert_to_milis(millis) -> str:
	total_seconds = millis / 1000
	hours = total_seconds / 3600
	minutes = (total_seconds % 3600) / 1000
	seconds = total_seconds % 60
	return f"{hours}: {minutes}: {seconds}"


convert_to_milis(1000)