Todos los archivos necesarios tales como Jquery, JavaScript, CSS3, y código HTML5 están listos Se encuentran en la carpeta lib.

1- La carpeta base-side contiene toda las partes necesarias para tener una plantilla con una barra lateral.

2- La carpeta base-top contiene todas las partes necesarias para tener una plantilla solo con una barra de navegación superior, con un diseño distinto al de base-side.

3- La carpeta top-side contiene todas las partes necesarias para tener una plantilla con una barra de navegación superior y lateral responsiva.

- IMPLEMENTACIÓN DEL DATATABLE -

<script src="{% static 'lib/datatables/js/jquery.dataTables.js' %}"></script> 
<script src="{% static 'lib/datatables/js/dataTables.bootstrap4.min.js' %}"></script>
<script src="{% static 'lib/datatables/plugins/responsive-2.2.3/js/dataTables.responsive.min.js' %}"></script>
<script src="{% static 'lib/datatables/plugins/responsive-2.2.3/js/responsive.bootstrap4.min.js' %}"></script>

Posteriormente colocar el siguiente código

<script type="text/javascript">
 table = $('#data').DataTable({
 responsive: true, 
}); </script>

el identificador $('#data') hace alusión a el id para la tabla que se quiere aplicar el datatable
