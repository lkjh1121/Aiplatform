function register_input() {
	const userWeight = document.getElementById('user-weight').value;
	const userCal = document.getElementById('user-cal').value;

	if (userWeight == '' || userCal == '') {
		alert("모든 란을 입력해주세요!");
	}else{
		window.location.href = `../home.html?${userWeight}?${userCal}`;
	}
}

function skip_input() {
	step = confirm("운동량 계산을 위한 정보 입력 입니다. 정말 건너뛰시겠습니까? \n(미입력시 70kg, 200kcal로 지정)");

	if (step) {
		window.location.href = `../home.html?70?200`;
	}
}