const shareBtn = document.getElementById('share-btn');

shareBtn.addEventListener('click', () => {
  navigator.clipboard.writeText(window.location.href);
  alert('The URL has been copied to your clipboard.')
});
