# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actividad(models.Model):
    actcod = models.AutoField(db_column='ActCod', primary_key=True)  # Field name made lowercase.
    actnom = models.CharField(db_column='ActNom', max_length=60)  # Field name made lowercase.
    actfecini = models.DateTimeField(db_column='ActfecIni', blank=True, null=True)  # Field name made lowercase.
    actfecfin = models.DateTimeField(db_column='ActFecFin', blank=True, null=True)  # Field name made lowercase.
    acttip = models.CharField(db_column='ActTip', max_length=20, blank=True, null=True)  # Field name made lowercase.
    acthortradia = models.TimeField(db_column='ActHorTraDia', blank=True, null=True)  # Field name made lowercase.
    estregcod = models.ForeignKey('EstadoRegistro', models.DO_NOTHING, db_column='EstRegCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actividad'


class ActividadesComplejidad(models.Model):
    actcod = models.OneToOneField(Actividad, models.DO_NOTHING, db_column='ActCod', primary_key=True)  # Field name made lowercase. The composite primary key (ActCod, ComCod) found, that is not supported. The first column is selected.
    comcod = models.ForeignKey('Complejidad', models.DO_NOTHING, db_column='ComCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actividades_complejidad'
        unique_together = (('actcod', 'comcod'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CargosPersonal(models.Model):
    carpercod = models.AutoField(db_column='CarPerCod', primary_key=True)  # Field name made lowercase.
    carpernom = models.CharField(db_column='CarPerNom', max_length=60, blank=True, null=True)  # Field name made lowercase.
    estregcod = models.ForeignKey('EstadoRegistro', models.DO_NOTHING, db_column='EstRegCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cargos_personal'


class CargosProyecto(models.Model):
    carprocod = models.AutoField(db_column='CarProCod', primary_key=True)  # Field name made lowercase.
    carpronom = models.CharField(db_column='CarProNom', max_length=60, blank=True, null=True)  # Field name made lowercase.
    prosec = models.ForeignKey('Proyecto', models.DO_NOTHING, db_column='ProSec')  # Field name made lowercase.
    estregcod = models.ForeignKey('EstadoRegistro', models.DO_NOTHING, db_column='EstRegCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cargos_proyecto'


class Cliente(models.Model):
    clidni = models.IntegerField(db_column='CliDni', primary_key=True)  # Field name made lowercase.
    clinom = models.CharField(db_column='CliNom', max_length=100)  # Field name made lowercase.
    clifecing = models.DateField(db_column='CliFecIng', blank=True, null=True)  # Field name made lowercase.
    clifecces = models.DateField(db_column='CliFecCes', blank=True, null=True)  # Field name made lowercase.
    clifecultprocer = models.DateField(db_column='CliFecUltProCer', blank=True, null=True)  # Field name made lowercase.
    clitipcod = models.ForeignKey('TipoCliente', models.DO_NOTHING, db_column='CliTipCod')  # Field name made lowercase.
    cliestcod = models.ForeignKey('EstadoCliente', models.DO_NOTHING, db_column='CliEstCod')  # Field name made lowercase.
    regestcod = models.ForeignKey('EstadoRegistro', models.DO_NOTHING, db_column='RegEstCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'


class Complejidad(models.Model):
    comcod = models.AutoField(db_column='ComCod', primary_key=True)  # Field name made lowercase.
    comnom = models.CharField(db_column='ComNom', max_length=60)  # Field name made lowercase.
    comgra = models.IntegerField(db_column='ComGra')  # Field name made lowercase.
    estregcod = models.ForeignKey('EstadoRegistro', models.DO_NOTHING, db_column='EstRegCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'complejidad'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EstadoCliente(models.Model):
    estclicod = models.AutoField(db_column='EstCliCod', primary_key=True)  # Field name made lowercase.
    estclinom = models.CharField(db_column='EstCliNom', max_length=60)  # Field name made lowercase.
    estcliestreg = models.CharField(db_column='EstCliEstReg', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado_cliente'


class EstadoProyecto(models.Model):
    estprocod = models.AutoField(db_column='EstProCod', primary_key=True)  # Field name made lowercase.
    estpronom = models.CharField(db_column='EstProNom', max_length=60)  # Field name made lowercase.
    estregcod = models.ForeignKey('EstadoRegistro', models.DO_NOTHING, db_column='EstRegCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado_proyecto'


class EstadoRegistro(models.Model):
    estregcod = models.AutoField(db_column='EstRegCod', primary_key=True)  # Field name made lowercase.
    estregnom = models.CharField(db_column='EstRegNom', max_length=60)  # Field name made lowercase.
    estregestreg = models.CharField(db_column='EstRegEstReg', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado_registro'


class EtapaActividad(models.Model):
    actcod = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='ActCod')  # Field name made lowercase.
    etaprocod = models.OneToOneField('EtapasProyecto', models.DO_NOTHING, db_column='EtaProCod', primary_key=True)  # Field name made lowercase. The composite primary key (EtaProCod, ActCod) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'etapa_actividad'
        unique_together = (('etaprocod', 'actcod'),)


class EtapasProyecto(models.Model):
    etaprocod = models.AutoField(db_column='EtaProCod', primary_key=True)  # Field name made lowercase.
    etapronom = models.CharField(db_column='EtaProNom', max_length=60)  # Field name made lowercase.
    etaprofecreg = models.DateTimeField(db_column='EtaProFecReg', blank=True, null=True)  # Field name made lowercase.
    etaprofecini = models.DateTimeField(db_column='EtaProFecIni', blank=True, null=True)  # Field name made lowercase.
    etaprofecfin = models.DateTimeField(db_column='EtaProFecFin', blank=True, null=True)  # Field name made lowercase.
    estregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, db_column='EstRegCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'etapas_proyecto'


class IncidenciaPersonal(models.Model):
    inccod = models.OneToOneField('Incidencias', models.DO_NOTHING, db_column='IncCod', primary_key=True)  # Field name made lowercase. The composite primary key (IncCod, PerCod) found, that is not supported. The first column is selected.
    percod = models.ForeignKey('Personal', models.DO_NOTHING, db_column='PerCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'incidencia_personal'
        unique_together = (('inccod', 'percod'),)


class Incidencias(models.Model):
    inccod = models.IntegerField(db_column='IncCod', primary_key=True)  # Field name made lowercase.
    incfecini = models.DateTimeField(db_column='IncFecIni')  # Field name made lowercase.
    incnom = models.CharField(db_column='IncNom', max_length=60, blank=True, null=True)  # Field name made lowercase.
    incfecfin = models.DateTimeField(db_column='IncFecFin', blank=True, null=True)  # Field name made lowercase.
    incdes = models.CharField(db_column='IncDes', max_length=60, blank=True, null=True)  # Field name made lowercase.
    actcod = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='ActCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'incidencias'


class Personal(models.Model):
    percod = models.AutoField(db_column='PerCod', primary_key=True)  # Field name made lowercase.
    pernom = models.CharField(db_column='PerNom', max_length=60)  # Field name made lowercase.
    percarcoshor = models.DecimalField(db_column='PerCarCosHor', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    perfecing = models.DateField(db_column='PerFecIng', blank=True, null=True)  # Field name made lowercase.
    estregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, db_column='EstRegCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personal'


class PersonalActividad(models.Model):
    actcod = models.OneToOneField(Actividad, models.DO_NOTHING, db_column='ActCod', primary_key=True)  # Field name made lowercase. The composite primary key (ActCod, PerCod) found, that is not supported. The first column is selected.
    percod = models.ForeignKey(Personal, models.DO_NOTHING, db_column='PerCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personal_actividad'
        unique_together = (('actcod', 'percod'),)


class PersonalCargosPersonal(models.Model):
    percod = models.OneToOneField(Personal, models.DO_NOTHING, db_column='PerCod', primary_key=True)  # Field name made lowercase. The composite primary key (PerCod, CarPerCod) found, that is not supported. The first column is selected.
    carpercod = models.ForeignKey(CargosPersonal, models.DO_NOTHING, db_column='CarPerCod')  # Field name made lowercase.
    percoshorcar = models.IntegerField(db_column='PerCosHorCar', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personal_cargos_personal'
        unique_together = (('percod', 'carpercod'),)


class PersonalCargosProyecto(models.Model):
    carprocod = models.OneToOneField(CargosProyecto, models.DO_NOTHING, db_column='CarProCod', primary_key=True)  # Field name made lowercase. The composite primary key (CarProCod, PerCod) found, that is not supported. The first column is selected.
    percod = models.ForeignKey(Personal, models.DO_NOTHING, db_column='PerCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personal_cargos_proyecto'
        unique_together = (('carprocod', 'percod'),)


class Proyecto(models.Model):
    prosec = models.AutoField(db_column='ProSec', primary_key=True)  # Field name made lowercase.
    profecprocon = models.DateField(db_column='ProFecProCon', blank=True, null=True)  # Field name made lowercase.
    profecpropac = models.DateField(db_column='ProFecProPac', blank=True, null=True)  # Field name made lowercase.
    profecproini = models.DateField(db_column='ProFecProIni', blank=True, null=True)  # Field name made lowercase.
    profecproent = models.DateField(db_column='ProFecProEnt', blank=True, null=True)  # Field name made lowercase.
    profecprocie = models.DateField(db_column='ProFecProCie', blank=True, null=True)  # Field name made lowercase.
    promonpro = models.DecimalField(db_column='ProMonPro', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    promonprorea = models.DecimalField(db_column='ProMonProRea', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    promonprocos = models.DecimalField(db_column='ProMonProCos', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    promonprocosrea = models.DecimalField(db_column='ProMonProCosRea', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    promonprogas = models.DecimalField(db_column='ProMonProGas', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    promonprogasrea = models.DecimalField(db_column='ProMonProGasRea', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    promonprouti = models.DecimalField(db_column='ProMonProUti', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    promonproutirea = models.DecimalField(db_column='ProMonProUtiRea', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    clicod = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='CliCod')  # Field name made lowercase.
    proestprocod = models.ForeignKey(EstadoProyecto, models.DO_NOTHING, db_column='ProEstProCod')  # Field name made lowercase.
    protipprocod = models.ForeignKey('TipoProyecto', models.DO_NOTHING, db_column='ProTipProCod')  # Field name made lowercase.
    proetaprocod = models.ForeignKey(EtapasProyecto, models.DO_NOTHING, db_column='ProEtaProCod')  # Field name made lowercase.
    estregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, db_column='EstRegCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proyecto'


class TipoCliente(models.Model):
    tipclicod = models.AutoField(db_column='TipCliCod', primary_key=True)  # Field name made lowercase.
    tipclinom = models.CharField(db_column='TipCliNom', max_length=60)  # Field name made lowercase.
    tipcliestreg = models.CharField(db_column='TipCliEstReg', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_cliente'


class TipoProyecto(models.Model):
    tipprocod = models.AutoField(db_column='TipProCod', primary_key=True)  # Field name made lowercase.
    tippronom = models.CharField(db_column='TipProNom', max_length=60)  # Field name made lowercase.
    estregcod = models.ForeignKey(EstadoRegistro, models.DO_NOTHING, db_column='EstRegCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_proyecto'
