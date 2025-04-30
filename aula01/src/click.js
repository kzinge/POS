botaonova = document.getElementById('botao')
botaofechar = document.getElementById('fechar')
form = document.getElementById('novatarefa')

botaonova.addEventListener('click', () =>{
    form.style.display = 'block';
})

botaofechar.addEventListener('click', () =>{
    form.style.display = 'none';
})