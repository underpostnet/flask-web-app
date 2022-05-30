
( async () => {


append('render', `


  <style>

      body {
        background: black;
        color: white;
        font-family: arial;
      }

      .content {
        border: 2px solid green;
        max-width: 500px;
        margin: auto;
        padding: 10px;
      }

      .btn-send {
        padding: 10px;
        cursor: pointer;
        background: green;
        transition: .3s;
        border: 2px solid green;
      }
      .btn-send:hover {
        border: 2px solid yellow;
      }

  </style>

  `+spr('<br>', 3)+`

      <div class='in content render-form'>

            <h1>Ingreso de Autos</h1>

      </div>

      <div class='in content render-list'>

            <h1>Registros</h1>

      </div>

  `+spr('<br>', 3)+`
`);


let parkings = await new Promise( resolve => {
  fetch("/parking_available", {
         method: "GET",
         headers: {
           "Content-Type": "application/json",
         },
         body: undefined,
       })
   .then((res) => res.json())
   .then((data) => resolve(data));
});

parkings =
parkings.map(x=>{
  return {
    value: x,
    display: x
  }
})

const inputs = [
  { name: "patente", type: "text" },
  { name: "hora_ingreso", type: "datetime-local" },
  { name: "hora_salida", type: "datetime-local" }
];
inputs.map(inputData => append('.render-form', renderInput({
    underpostClass: 'in',
    id_content_input: makeid(5),
    id_input: inputData.name,
    type: inputData.type,
    required: true,
    style_content_input: '',
    style_input: 'color: black; font-size: 16px; padding: 10px',
    style_label: '',
    style_outline: true,
    style_placeholder: '',
    textarea: false,
    active_label: false,
    initLabelPos: 15,
    endLabelPos: -30,
    text_label: '',
    tag_label: makeid(5),
    fnOnClick: async () => {
      console.log('click input');
    },
    value: ``,
    topContent: inputData.type == 'datetime-local' ? cap(inputData.name.replaceAll('_', ' ')) : '',
    botContent: '<br>',
    placeholder: cap(inputData.name.replaceAll('_', ' '))
  })));

  append('.render-form', renderDropDownV1({
    title: 'Seleccione Estacionamiento',
    id: "estacionamiento",
    underpostClass: 'in',
    style: {
      content: 'font-size: 14px; padding: 10px;',
      option: 'font-size: 14px; padding: 10px;'
    },
    data: parkings
  }));

  append('.render-form', `
     `+spr('<br>', 1)+`
      <div class='inl btn-send'>
          ENVIAR
      </div>
      `+spr('<br>', 1)+`
  `);


  s('.btn-send').onclick = () => {

      const postObj = {
        patente: s('.patente').value,
        hora_ingreso: s('.hora_ingreso').value,
        hora_salida: s('.hora_salida').value,
        estacionamiento: s('.estacionamiento').value
      };
      console.log("postObj", postObj);



    fetch("/order_car", {
           method: "POST",
           headers: {
             "Content-Type": "application/json",
           },
           body: JSON.stringify(postObj),
         })
     .then((res) => res.json())
     .then((data) => console.log(data));

  };


})()
