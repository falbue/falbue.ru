function toggleTheme() {
  const root = document.documentElement;
  const currentTheme = root.style.getPropertyValue('--bg-main') === '#cdbce2' ? 'dark' : 'light';

  if (currentTheme === 'dark') {
    root.style.setProperty('--bg-main', '#1A1A36');
    root.style.setProperty('--text-color', '#cdbce2');
    root.style.setProperty('--bg-second', '#2E2661');
  } else {
    root.style.setProperty('--bg-main', '#cdbce2');
    root.style.setProperty('--text-color', '#1A1A36');
    root.style.setProperty('--bg-second', '#af99cc');
  }
}