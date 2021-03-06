function comunasgenerate(){
    var regionesConComunas = {
        "": ["Seleccione su Comuna"],
        "Región Metropolitana de Santiago": ["Seleccione su Comuna","Cerrillos", "Cerro Navia", "Conchalí", "El Bosque", "Estación Central", "Huechuraba", "Independencia", "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "Ñuñoa", "Pedro Aguirre Cerda", "Peñalolén", "Providencia", "Pudahuel", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "San Joaquín", "San Miguel", "San Ramón", "Vitacura", "Puente Alto", "Pirque", "San José de Maipo", "Colina", "Lampa", "Tiltil", "San Bernardo", "Buin", "Calera de Tango", "Paine", "Melipilla", "Alhué", "Curacaví", "María Pinto", "San Pedro", "Talagante", "El Monte", "Isla de Maipo", "Padre Hurtado", "Peñaflor"],
        "Región de Arica y Parinacota": ["Seleccione su Comuna","Arica", "Camarones", "Putre", "General Lagos"],
        "Región de Tarapacá": ["Seleccione su Comuna","Iquique", "Alto Hospicio", "Pozo Almonte", "Camiña", "Colchane", "Huara", "Pica"],
        "Región de Antofagasta": ["Seleccione su Comuna","Antofagasta", "Mejillones", "Sierra Gorda", "Taltal", "Calama", "Ollagüe", "San Pedro de Atacama", "Tocopilla", "María Elena"],
        "Región de Atacama": ["Seleccione su Comuna","Copiapó", "Caldera", "Tierra Amarilla", "Chañaral", "Diego de Almagro", "Vallenar", "Alto del Carmen", "Freirina", "Huasco"],
        "Región de Coquimbo": ["Seleccione su Comuna","La Serena", "Coquimbo", "Andacollo", "La Higuera", "Paiguano", "Vicuña", "Illapel", "Canela", "Los Vilos", "Salamanca", "Ovalle", "Combarbalá", "Monte Patria", "Punitaqui", "Río Hurtado"],
        "Región de Valparaíso": ["Seleccione su Comuna","Valparaíso", "Casablanca", "Concón", "Juan Fernández", "Puchuncaví", "Quintero", "Viña del Mar", "Isla de Pascua", "Los Andes", "Calle Larga", "Rinconada", "San Esteban", "La Ligua", "Cabildo", "Papudo", "Petorca", "Zapallar", "Quillota", "Calera", "Hijuelas", "La Cruz", "Nogales", "San Antonio", "Algarrobo", "Cartagena", "El Quisco", "El Tabo", "Santo Domingo", "San Felipe", "Catemu", "Llaillay", "Panquehue", "Putaendo", "Santa María", "Quilpué", "Limache", "Olmué", "Villa Alemana"],
        "Región del Libertador Gral. Bernardo O Higgins": ["Seleccione su Comuna","Rancagua", "Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "Las Cabras", "Machalí", "Malloa", "Mostazal", "Olivar", "Peumo", "Pichidegua", "Quinta de Tilcoco", "Rengo", "Requínoa", "San Vicente", "Pichilemu", "La Estrella", "Litueche", "Marchihue", "Navidad", "Paredones", "San Fernando", "Chépica", "Chimbarongo", "Lolol", "Nancagua", "Palmilla", "Peralillo", "Placilla", "Pumanque", "Santa Cruz"],
        "Región del Maule": ["Seleccione su Comuna","Talca", "Constitución", "Curepto", "Empedrado", "Maule", "Pelarco", "Pencahue", "Río Claro", "San Clemente", "San Rafael", "Cauquenes", "Chanco", "Pelluhue", "Curicó", "Hualañé", "Licantén", "Molina", "Rauco", "Romeral", "Sagrada Familia", "Teno", "Vichuquén", "Linares", "Colbún", "Longaví", "Parral", "Retiro", "San Javier", "Villa Alegre", "Yerbas Buenas"],
        "Región de Ñuble": ["Seleccione su Comuna","Cobquecura", "Coelemu", "Ninhue", "Portezuelo", "Quirihue", "Ránquil", "Treguaco", "Bulnes", "Chillán Viejo", "Chillán", "El Carmen", "Pemuco", "Pinto", "Quillón", "San Ignacio", "Yungay", "Coihueco", "Ñiquén", "San Carlos", "San Fabián", "San Nicolás"],
        "Región del Biobío": ["Seleccione su Comuna","Alto Biobío","Antuco","Arauco","Cabrero","Cañete","Chiguayante","Concepción","Contulmo","Coronel","Curanilahue","Florida","Hualpén","Hualqui","Laja","Lebu","Los Álamos","Los Ángeles","Lota","Mulchén","Nacimiento","Negrete","Penco","Quilaco","Quilleco","San Pedro de la Paz","San Rosendo","Santa Bárbara","Santa Juana","Talcahuano","Tirúa","Tomé","Tucapel", "Yumbel"],
        "Región de la Araucanía": ["Seleccione su Comuna","Temuco", "Carahue", "Cunco", "Curarrehue", "Freire", "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Melipeuco", "Nueva Imperial", "Padre las Casas", "Perquenco", "Pitrufquén", "Pucón", "Saavedra", "Teodoro Schmidt", "Toltén", "Vilcún", "Villarrica", "Cholchol", "Angol", "Collipulli", "Curacautín", "Ercilla", "Lonquimay", "Los Sauces", "Lumaco", "Purén", "Renaico", "Traiguén", "Victoria"],
        "Región de Los Ríos": ["Seleccione su Comuna","Valdivia", "Corral", "Lanco", "Los Lagos", "Máfil", "Mariquina", "Paillaco", "Panguipulli", "La Unión", "Futrono", "Lago Ranco", "Río Bueno"],
        "Región de Los Lagos": ["Seleccione su Comuna","Puerto Montt", "Calbuco", "Cochamó", "Fresia", "Frutillar", "Los Muermos", "Llanquihue", "Maullín", "Puerto Varas", "Castro", "Ancud", "Chonchi", "Curaco de Vélez", "Dalcahue", "Puqueldón", "Queilén", "Quellón", "Quemchi", "Quinchao", "Osorno", "Puerto Octay", "Purranque", "Puyehue", "Río Negro", "San Juan de la Costa", "San Pablo", "Chaitén", "Futaleufú", "Hualaihué", "Palena"],
        "Región Aisén del Gral. Carlos Ibáñez del Campo": ["Seleccione su Comuna","Coihaique", "Lago Verde", "Aisén", "Cisnes", "Guaitecas", "Cochrane", "O Higgins", "Tortel", "Chile Chico", "Río Ibáñez"],
        "Región de Magallanes y de la Antártica Chilena": ["Seleccione su Comuna","Punta Arenas", "Laguna Blanca", "Río Verde", "San Gregorio", "Cabo de Hornos (Ex Navarino)", "Antártica", "Porvenir", "Primavera", "Timaukel", "Natales", "Torres del Paine"]
      }
    var region=document.getElementById("region").value;
    var comunas=document.getElementById("comuna");
    for(var i = comunas.options.length; i > 0; i--) {
        comunas.options[i - 1].remove();
      }
    regionesConComunas[region].forEach(function(item) {
        var option = new Option(item, item);
        comunas.appendChild(option);
      });
}

function agrandar(el){
    var modal= document.getElementById("myModal");
    var modalImg = document.getElementById("img01");
    modal.style.display = "block";
    modalImg.src = el.src;
}

function achicar(id){
    var modal= document.getElementById(id);
    modal.style.display = "none";
}

function achicarDos(){
    achicar('modalConfirmacion');
    achicar('modalForm');
}

function abrir(id){
    var modal= document.getElementById(id);
    modal.style.display = "block";
}

function duplicar(el,th){
    if (el!="foto-mascota"){
        var original= document.getElementById(el);
        var duplicado= original.cloneNode(true);
        duplicado.id="";
        duplicado.style.display="block";
        original.parentNode.appendChild(duplicado);
    }
    else{
        var count=0;
        document.getElementsByName("foto-mascota").forEach(function(element){
            if (element.parentNode==th.parentNode){
                count=count+1;
            }
        });
        if (count<5){
            var original= document.getElementById(el);
            var duplicado= original.cloneNode(true);
            duplicado.id="";
            duplicado.style.display="block";
            th.parentNode.appendChild(duplicado); 
        }
    }
}

function addOtro(el){
    var value="";
    var forms=document.getElementsByName("tipo-mascota").forEach(function(element){
        if (element.parentNode==el.parentNode){
            value=element.value;
        }
    });

    if (value=="otro"){
        document.getElementsByName("tipo-mascota-otro").forEach(function(element){
            if (element.parentNode==el.parentNode){
                element.style.display="block";
            } 
        });
    }
    else{
        document.getElementsByName("tipo-mascota-otro").forEach(function(element){
            if (element.parentNode==el.parentNode){
                element.style.display="none";
            } 
        });
    }    
}

function mostrarError(msg) {

    let contenedor = document.getElementById('error');

    contenedor.innerHTML = msg;
    contenedor.style.display = 'block';
}

/**
 Validacion del formulario
 */


function validar() {
    var mensaje = "";

    if(document.getElementById("region").value==""){
        mensaje +="<br>";
        mensaje += "- Seleccione su Región";
    }

    if(document.getElementById("comuna").value==""||document.getElementById("comuna").value=="Seleccione su Comuna"){
        mensaje +="<br>";
        mensaje += "- Seleccione su Comuna";
    }

    document.getElementsByName("tipo-mascota").forEach(function(element){
        if (element.parentElement.parentElement.id!="infomascota"){
        
            if (element.value==""){
                mensaje +="<br>";
                mensaje += "- Seleccione el tipo de su mascota";
            }
            if (element.value=="otro"){
                document.getElementsByName("tipo-mascota-otro").forEach(function(el){
                    if (el.parentNode==element.parentNode && (el.value==""||el.length>40)){
                        mensaje +="<br>";
                        mensaje += "- Ingrese un tipo válido para su mascota";  
                    } 
                });
        }
    }
    });

    document.getElementsByName("foto-mascota").forEach(function(element){
        if (element.parentElement.parentElement.id!="infomascota"){
        if(element.value==""){
            mensaje +="<br>";
            mensaje += "- Suba una foto de su mascota";
        }
    }
    });
    if (mensaje.length < 1){
        achicar('modalForm')
        return true;
    }

    mostrarError("Se han encontrado los siguientes errores:"+ mensaje)
    return false;

}

console.log('app v1.0'); // stack trace