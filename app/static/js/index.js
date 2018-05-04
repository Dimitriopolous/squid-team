function submitVals() {
	let file = new File("../../../actors.json");
	let arr = [];
	arr.push({
		"actor1": getElementsByName("actor1").value,
		"actor2": getElementsByName("actor2").value
	});
	file.open("w");
	file.write(arr);
	file.close();
}
