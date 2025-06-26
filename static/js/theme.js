function toggleTheme() {
  const htmlElement = document.documentElement;
  const isDark = htmlElement.classList.contains('dark-theme');
  
  if (isDark) {
    htmlElement.classList.remove('dark-theme');
    localStorage.setItem('theme', 'light');
  } else {
    htmlElement.classList.add('dark-theme');
    localStorage.setItem('theme', 'dark');
  }
}

// Инициализация темы при загрузке
function initTheme() {
  const savedTheme = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  
  if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
    document.documentElement.classList.add('dark-theme');
  }
}

// Запускаем при загрузке страницы
window.addEventListener('DOMContentLoaded', initTheme);