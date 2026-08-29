const trainingEl = document.getElementById('training-el');
trainingEl.addEventListener('click', function() {
    window.location.href = "/play"
});

const nextScenario =document.getElementById('next-scenario')
nextScenario.addEventListener('click', function(){
    window.location.href = "/play?next=1"
})

const answerEl = document.getElementById('answer-el');
const inputEl = document.getElementById('input-el')
answerEl.addEventListener('click', function(){
    answerEl.disabled = "true"
})
inputEl.addEventListener('click', function(){
    inputEl.disabled = "true"
})