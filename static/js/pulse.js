let boxShadowValue = 80; // Начальное значение
let increasing = true; // Увеличиваем ли значение
const speed = 100; // Скорость изменения (в миллисекундах)
const minShadow = 20; // Минимальное значение box-shadow
const maxShadow = 80; // Максимальное значение box-shadow

function updateBoxShadow() {
	const box = document.getElementById('myBox');
	box.style.boxShadow = `0px 0px ${boxShadowValue}px var(--text-color)`;

	if (increasing) {
		boxShadowValue += 1;
		if (boxShadowValue >= maxShadow) {
			increasing = false;
		}
	} else {
		boxShadowValue -= 1;
		if (boxShadowValue <= minShadow) {
			increasing = true;
		}
	}
}

setInterval(updateBoxShadow, speed);