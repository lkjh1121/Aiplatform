const snackArr = ['오예스', '몽쉘', '카스타드', '참쌀설병', '참쌀선과', '참크래커', '로투스', 'abc초콜렛', '커피믹스', '카누', '핫초코'];
const snackCalArr = [150, 155, 105, 45, 25, 90, 30, 16.95, 50, 3, 85];
const eatCalArr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
const date = new Date();
let totalCal = 0;
let seqNum = 1;

function changeOption() {
	const selectType = document.getElementById('combo-type').value;
	if (selectType == "minus") {
		document.getElementById("plus-option1").style.display = "none";
		document.getElementById("plus-option2").style.display = "none";
		document.getElementById('delete-info').style.display = "block";
	}else  {
		document.getElementById("plus-option1").style.display = "block";
		document.getElementById("plus-option2").style.display = "block";
		document.getElementById('delete-info').style.display = "none";

	}
}

function snack_input(){
	const selectType = document.getElementById('combo-type').value;

	if (selectType == "plus"){
		const snackName = document.getElementById('snack-name').value;
		const snackCount = document.getElementById('snack-count').value;
		let input_snack = snackName.replace(/(\s*)/g, "");
		let idx = snackArr.indexOf(input_snack);

		if (idx >= 0){
			totalCal += parseInt(snackCalArr[idx]*parseInt(snackCount));
			eatInformation(snackArr[idx], snackCalArr[idx]*parseInt(snackCount), snackCount, totalCal, selectType);
		}
		else{
			let equalArr = [];
			for (let i=0; i<snackArr.length; i++){
				equalArr[i] = 0;
			}
			for (i=0; i<input_snack.length; i++){
				for (j=0; j<snackArr.length; j++){
					let regex = new RegExp(`${input_snack[i]}`, 'g');
					let result = snackArr[j].match(regex);
					if (result != null) {
						equalArr[j] += result.length;
					}
				}
			}
			const maxVal = Math.max.apply(null, equalArr);
			let count = equalArr.reduce((cnt, element) => cnt + (maxVal === element), 0);
			if (maxVal > 0 && count == 1){
				idx = equalArr.indexOf(maxVal);
				confirmValue = confirm(`혹시 찾으시는 과자가 ${snackArr[idx]}가 맞나요?`);
				if (confirmValue) {
					totalCal += snackCalArr[idx]*parseInt(snackCount);
					eatInformation(snackArr[idx], snackCalArr[idx]*parseInt(snackCount), snackCount, totalCal, selectType);
				}else {
					alert("일치하는 간식 이름이 없어요! 다시 입력해주세요.");
				}
			}else{
				alert("일치하는 간식 이름이 없어요! 다시 입력해주세요.");
			}
		}
		document.getElementById('snack-name').value = "";
		document.getElementById('snack-count').value = "";
		document.getElementById('combo-type').value = "none";
	}else {
		const deleteRow = document.getElementById('delete-row').value;
		const table = document.getElementById('eat-info');
		let rows = table.rows;
		const rowCount = rows.length;

		if (rowCount == 1) {
			alert("아직 아무런 정보가 등록되지 않았습니다.");
			document.getElementById('delete-row').value = "";
		}else{
			if (deleteRow > rowCount-1 || deleteRow < 1){
				alert("존재하지 않는 행번호 입니다.");
			}else{
				const flag = confirm("정말 삭제하시겠습니까?");
				if (flag){
					let delCells = rows[parseInt(deleteRow)].cells[4].innerText.split("k")[0];
					let pastCells = 0;
					table.deleteRow(deleteRow);
					document.getElementById('delete-row').value = "";
					
					if (parseInt(deleteRow) > 1) {
						pastCells = rows[parseInt(deleteRow)-1].cells[4].innerText.split("k")[0];
					}
					if (parseInt(deleteRow) == rows.length){
						totalCal = pastCells;
					}else{
						for (let i=parseInt(deleteRow); i<rows.length; i++) {
							let curCells = rows[i].cells[4].innerText.split("k")[0];
							
							rows[i].cells[4].innerText = `${curCells - delCells + parseInt(pastCells)}kcal`;
							totalCal = curCells - delCells + parseInt(pastCells);
						}
					}
					notificationInfo(totalCal);
					if (rowCount == 2) {
						document.getElementById("guide1").style.display = "block";
						document.getElementById("guide2").style.display = "block";
						document.getElementById("guide3").style.display = "block";
						document.getElementById("eat-info").style.display = "none";
						document.getElementById("notice-info").style.display = "none";
						document.getElementById("img-zone").style.display = "none";
					}
				}
				document.getElementById('delete-row').value = "";
			}
		}
	}
}

function eatInformation(eatName, eatCal, eatCount, totalCal, whatType) {
	document.getElementById('snack-name').value = "";
	document.getElementById('snack-count').value = "";
	document.getElementById('combo-type').value = "none";

	let html = '';
	const year = date.getFullYear();
	const month = ('0' + (date.getMonth() + 1)).slice(-2);
	const day = ('0' + date.getDate()).slice(-2);
	const hours = ('0' + date.getHours()).slice(-2);
	const minutes = ('0' + date.getMinutes()).slice(-2);
	const seconds = ('0' + date.getSeconds()).slice(-2);
	const timeStr = year + '-' + month + '-' + day + ' ' + hours + ':' + minutes + ':' + seconds;

	document.getElementById("guide1").style.display = "none";
	document.getElementById("eat-info").style.display = "block";

	if (whatType == 'plus') {
		html += '<tr>';
		html += '<td>'+timeStr+'</td>';
	  	html += '<td>'+eatName+'</td>';
		html += '<td>'+eatCount+'개</td>';
		html += '<td>'+eatCal+'kcal</td>';
	  	html += '<td>'+totalCal+'kcal</td>';
	  	html += '</tr>';

	  	document.getElementById('eat-info').innerHTML += html;
	  	notificationInfo(totalCal);
	}
}

function notificationInfo(calInfo) {
	let idArr = ['running', 'cycle', 'situp'];
	let exerciseArr = ['달리기(8km/h)', '자전거타기(15~20km/hr)', '수영'];
	let exerciseCal = [0.13, 0.1, 0.13];
	const receivedDataWeight = location.href.split('?')[1];
	const receivedDataCal = location.href.split('?')[2];
	let cmd = ''; 

	document.getElementById("guide2").style.display = "none";
	document.getElementById("notice-info").style.display = "block";
	
	if (receivedDataCal-calInfo > 0){
		cmd += '<h3>남은 칼로리 : '+(receivedDataCal-calInfo)+'kcal</h3>'
		document.getElementById('notice-info').innerHTML = cmd;
		document.getElementById("guide3").style.display = "block";
		document.getElementById("img-zone").style.display = "none";
	}else{
		cmd += '<h3>초과한 칼로리 : '+(calInfo - receivedDataCal)+'kcal</h3>'
		cmd += '<img src=images/pig.gif id="pig">'
		document.getElementById('notice-info').innerHTML = cmd;

		document.getElementById("guide3").style.display = "none";
		document.getElementById("img-zone").style.display = "block";

		for (let i=0; i<exerciseCal.length; i++) {
			document.getElementById(idArr[i]).innerHTML = `<img src='images/${idArr[i]}.png'><div>${exerciseArr[i]}</div><div>${Math.round((calInfo - receivedDataCal) / (exerciseCal[i]*receivedDataWeight))}분</div>`;
		}
	}
}