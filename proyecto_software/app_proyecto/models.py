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
    actcomcod = models.AutoField(db_column='ActComCod', primary_key=True)  # Field name made lowercase.
    actcod = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='ActCod')  # Field name made lowercase.
    comcod = models.ForeignKey('Complejidad', models.DO_NOTHING, db_column='ComCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actividades_complejidad'


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
    etaactcod = models.AutoField(db_column='EtaActCod', primary_key=True)  # Field name made lowercase.
    actcod = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='ActCod')  # Field name made lowercase.
    etaprocod = models.ForeignKey('EtapasProyecto', models.DO_NOTHING, db_column='EtaProCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'etapa_actividad'


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
    incpercod = models.AutoField(db_column='IncPerCod', primary_key=True)  # Field name made lowercase.
    inccod = models.ForeignKey('Incidencias', models.DO_NOTHING, db_column='IncCod')  # Field name made lowercase.
    percod = models.ForeignKey('Personal', models.DO_NOTHING, db_column='PerCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'incidencia_personal'


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
    peractcod = models.AutoField(db_column='PerActCod', primary_key=True)  # Field name made lowercase.
    actcod = models.ForeignKey(Actividad, models.DO_NOTHING, db_column='ActCod')  # Field name made lowercase.
    percod = models.ForeignKey(Personal, models.DO_NOTHING, db_column='PerCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personal_actividad'


class PersonalCargosPersonal(models.Model):
    percarpercod = models.AutoField(db_column='PerCarPerCod', primary_key=True)  # Field name made lowercase.
    percod = models.ForeignKey(Personal, models.DO_NOTHING, db_column='PerCod')  # Field name made lowercase.
    carpercod = models.ForeignKey(CargosPersonal, models.DO_NOTHING, db_column='CarPerCod')  # Field name made lowercase.
    percoshorcar = models.IntegerField(db_column='PerCosHorCar', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personal_cargos_personal'


class PersonalCargosProyecto(models.Model):
    percarprocod = models.AutoField(db_column='PerCarProCod', primary_key=True)  # Field name made lowercase.
    carprocod = models.ForeignKey(CargosProyecto, models.DO_NOTHING, db_column='CarProCod')  # Field name made lowercase.
    percod = models.ForeignKey(Personal, models.DO_NOTHING, db_column='PerCod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'personal_cargos_proyecto'


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
