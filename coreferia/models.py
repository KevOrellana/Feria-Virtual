# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    rut = models.CharField(primary_key=True, max_length=12)
    nombre_comp = models.CharField(max_length=250)
    fecha_nac = models.DateField()
    correo = models.CharField(max_length=250)
    telefono = models.FloatField()
    auth_user_username = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'administrador'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bodega(models.Model):
    cod_bodega = models.FloatField(primary_key=True)
    capacidad = models.FloatField()
    direccion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'bodega'


class ClExterno(models.Model):
    rut = models.CharField(primary_key=True, max_length=12)
    nom_comp = models.CharField(max_length=250)
    fecha_nac = models.DateField()
    pais = models.CharField(max_length=250)
    telefono = models.FloatField()
    direccion = models.CharField(max_length=250)
    correo = models.CharField(max_length=250)
    auth_user_username = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'cl_externo'


class ClInterno(models.Model):
    rut = models.CharField(primary_key=True, max_length=12)
    nom_comp = models.CharField(max_length=250)
    fecha_nac = models.DateField()
    direccion = models.CharField(max_length=250)
    telefono = models.FloatField()
    correo = models.CharField(max_length=250)
    auth_user_username = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'cl_interno'


class Consultor(models.Model):
    rut = models.CharField(primary_key=True, max_length=12)
    nombre_comp = models.CharField(max_length=250)
    correo = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    telefono = models.FloatField()
    auth_user_username = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'consultor'


class ContratoP(models.Model):
    cod_contrato = models.FloatField(primary_key=True)
    fecha_termino_contrato = models.DateField()
    fecha_inicio_contrato = models.DateField()
    productor_rut = models.ForeignKey('Productor', models.DO_NOTHING, db_column='productor_rut')
    status = models.FloatField()

    class Meta:
        managed = False
        db_table = 'contrato_p'


class ContratoT(models.Model):
    cod_contrato = models.FloatField(primary_key=True)
    fecha_termino_contrato = models.DateField()
    fecha_inicio_contrato = models.DateField()
    transportista_rut = models.ForeignKey('Transportista', models.DO_NOTHING, db_column='transportista_rut')
    status = models.FloatField()

    class Meta:
        managed = False
        db_table = 'contrato_t'


class DetalleFactura(models.Model):
    detalle_factura_id = models.FloatField(primary_key=True)
    cantidad = models.FloatField()
    subtotal = models.FloatField()
    id_orden = models.ForeignKey('Orden', models.DO_NOTHING, db_column='id_orden')

    class Meta:
        managed = False
        db_table = 'detalle_factura'


class DetalleOrden(models.Model):
    id_orden = models.ForeignKey('Orden', models.DO_NOTHING, db_column='id_orden')
    cod_prod = models.ForeignKey('Producto', models.DO_NOTHING, db_column='cod_prod')
    cantidad = models.FloatField()
    precio = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detalle_orden'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Factura(models.Model):
    cod_fact = models.FloatField()
    cantidad = models.FloatField()
    total = models.FloatField()
    detalle_factura_id = models.FloatField()
    registro_pago_id_pago = models.FloatField()
    auth_user_username = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='auth_user_username')

    class Meta:
        managed = False
        db_table = 'factura'


class OfertaT(models.Model):
    cod_ot = models.FloatField(primary_key=True)
    tipo_vehiculo = models.CharField(max_length=250)
    tamano_veh = models.CharField(max_length=259)
    capacidad_carga = models.FloatField()
    refrigeracion = models.FloatField()
    ventilacion = models.FloatField()
    precio_transporte = models.FloatField()
    transportista_rut = models.ForeignKey('Transportista', models.DO_NOTHING, db_column='transportista_rut')

    class Meta:
        managed = False
        db_table = 'oferta_t'


class Orden(models.Model):
    id_orden = models.FloatField(primary_key=True)
    auth_user_username = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='auth_user_username')
    cantidad_total = models.FloatField()
    precio_total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'orden'


class Pedido(models.Model):
    cod_pedido = models.FloatField(primary_key=True)
    estado_pedido = models.CharField(max_length=10)
    descripcion_pedido = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'pedido'


class Perfil(models.Model):
    id_perfil = models.FloatField()
    descripcion = models.CharField(max_length=100)
    auth_user_username = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='auth_user_username')

    class Meta:
        managed = False
        db_table = 'perfil'


class Producto(models.Model):
    cod_prod = models.FloatField(primary_key=True)
    nom_prod = models.CharField(max_length=200)
    fecha_prod = models.DateField()
    foto_prod = models.ImageField(blank=True, null=True, upload_to='media/productos')
    precio = models.FloatField()
    cantidad = models.FloatField()
    productor_rut = models.ForeignKey('Productor', models.DO_NOTHING, db_column='productor_rut')

    class Meta:
        managed = False
        db_table = 'producto'


class Productor(models.Model):
    rut = models.CharField(primary_key=True, max_length=12)
    nombre_completo = models.CharField(max_length=250)
    fecha_nac = models.DateField()
    correo = models.CharField(max_length=250)
    telefono = models.FloatField()
    direccion = models.CharField(max_length=250)
    auth_user_username = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'productor'


class RegistroPago(models.Model):
    id_pago = models.FloatField(primary_key=True)
    total = models.FloatField()
    cod_fact = models.FloatField()

    class Meta:
        managed = False
        db_table = 'registro_pago'


class RegistroProcesoUsuario(models.Model):
    nombre_usuario = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'registro_proceso_usuario'


class RegistroProcesosAdmin(models.Model):
    nombre_admin = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'registro_procesos_admin'


class Reporte(models.Model):
    cod_reporte = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=250)
    factura_cod_fact = models.FloatField()

    class Meta:
        managed = False
        db_table = 'reporte'


class Subasta(models.Model):
    cod_subasta = models.FloatField(primary_key=True)
    fecha_subasta = models.DateField()
    transporte = models.CharField(max_length=250)
    nombre_completo = models.CharField(max_length=250)
    tamano_transporte = models.CharField(max_length=250)
    capacidad = models.FloatField()
    refrigeracion = models.FloatField()
    ventilacion = models.FloatField()
    precio_transporte = models.FloatField()
    id_orden = models.ForeignKey(Orden, models.DO_NOTHING, db_column='id_orden')
    oferta_t_cod_ot = models.FloatField()
    bodega_cod_bodega = models.FloatField()
    rut_transportista = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'subasta'


class Transportista(models.Model):
    transportista_rut = models.CharField(primary_key=True, max_length=12)
    nombre_comp = models.CharField(max_length=250)
    fecha_nac = models.DateField()
    telefono = models.FloatField()
    correo = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    patente_vehiculo = models.CharField(max_length=250)
    tipo_licencia = models.CharField(max_length=250)
    descripcion_vehiculo = models.CharField(max_length=250)
    auth_user_username = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'transportista'
