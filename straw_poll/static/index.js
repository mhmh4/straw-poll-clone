// let options = document.getElementById('options');
// console.log(options.children);
// let foo = options;
// console.log(foo)
// // foo.addEventListener("click", () => {
// //   console.log('hello');
// //   options.innerHTML += (`<li><input type="text" name="" id="" placeholder="Enter poll option"></li>`);
// // });


const shareBtn = document.getElementById("share-btn");

shareBtn.addEventListener("click", () => {
    navigator.clipboard.writeText(window.location.href);
    alert("The url has been copied to your clipboard.")
});
