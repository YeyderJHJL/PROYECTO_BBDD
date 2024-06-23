from django.db import models

class EstadoRegistro(models.Model): # listo
    estregcod = models.AutoField(db_column='EstRegCod', primary_key=True, verbose_name="Código")
    estregnom = models.CharField(db_column='EstRegNom', max_length=60, verbose_name="Nombre")
    estregestreg = models.CharField(db_column='EstRegEstReg', max_length=20, blank=True, null=True, verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Estado de Registro"
        verbose_name_plural = "Estados de Registro"
        db_table = 'estado_registro'

    def __str__(self):
        return self.estregnom

class TipoCliente(models.Model):
    tipclicod = models.AutoField(db_column='TipCliCod', primary_key=True, verbose_name="Código")
    tipclinom = models.CharField(db_column='TipCliNom', max_length=60, verbose_name="Nombre")
    tipcliestreg = models.CharField(db_column='TipCliEstReg', max_length=20, blank=True, null=True, verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Tipo de Cliente"
        verbose_name_plural = "Tipos de Cliente"
        db_table = 'tipo_cliente'

    def __str__(self):
        return self.tipclinom

class EstadoCliente(models.Model):
    estclicod = models.AutoField(db_column='EstCliCod', primary_key=True, verbose_name="Código")
    estclinom = models.CharField(db_column='EstCliNom', max_length=60, verbose_name="Nombre")
    estcliestreg = models.CharField(db_column='EstCliEstReg', max_length=20, blank=True, null=True, verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Estado de Cliente"
        verbose_name_plural = "Estados de Cliente"
        db_table = 'estado_cliente'

    def __str__(self):
        return f"{self.estclinom}"

class Cliente(models.Model): # listo
    clidni = models.IntegerField(db_column='CliDni', primary_key=True, verbose_name="DNI")
    clinom = models.CharField(db_column='CliNom', max_length=100, verbose_name="Nombre")
    clifecing = models.DateField(db_column='CliFecIng', blank=True, null=True, verbose_name="Fecha de Ingreso")
    clifecces = models.DateField(db_column='CliFecCes', blank=True, null=True, verbose_name="Fecha de Cese")
    clifecultprocer = models.DateField(db_column='CliFecUltProCer', blank=True, null=True, verbose_name="Fecha Último Proyecto Cerrado")
    clitipcod = models.ForeignKey(TipoCliente, on_delete=models.PROTECT, db_column='CliTipCod', verbose_name="Tipo de Cliente")
    cliestcod = models.ForeignKey(EstadoCliente, on_delete=models.PROTECT, db_column='CliEstCod', verbose_name="Estado de Cliente")
    regestcod = models.ForeignKey(EstadoRegistro, on_delete=models.PROTECT, db_column='RegEstCod', verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        db_table = 'cliente'

    def __str__(self):
        return f"{self.clinom} (DNI: {self.clidni})"

class CargosPersonal(models.Model): # listo
    carpercod = models.AutoField(db_column='CarPerCod', primary_key=True, verbose_name="Código")
    carpernom = models.CharField(db_column='CarPerNom', max_length=60, verbose_name="Nombre")
    estregcod = models.ForeignKey(EstadoRegistro, on_delete=models.PROTECT, db_column='EstRegCod', verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Cargo de Personal"
        verbose_name_plural = "Cargos de Personal"
        db_table = 'cargos_personal'

    def __str__(self):
        return self.carpernom

class Personal(models.Model):
    percod = models.AutoField(db_column='PerCod', primary_key=True, verbose_name="Código")
    pernom = models.CharField(db_column='PerNom', max_length=60, verbose_name="Nombre")
    percarcoshor = models.DecimalField(db_column='PerCarCosHor', max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Costo por Hora")
    perfecing = models.DateField(db_column='PerFecIng', blank=True, null=True, verbose_name="Fecha de Ingreso")
    estregcod = models.ForeignKey(EstadoRegistro, on_delete=models.PROTECT, db_column='EstRegCod', verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personal"
        db_table = 'personal'

    def __str__(self):
        return self.pernom

class PersonalCargosPersonal(models.Model):
    percarpercod = models.AutoField(db_column='PerCarPerCod', primary_key=True, verbose_name="Código")
    percod = models.ForeignKey(Personal, on_delete=models.CASCADE, db_column='PerCod', verbose_name="Personal")
    carpercod = models.ForeignKey(CargosPersonal, on_delete=models.CASCADE, db_column='CarPerCod', verbose_name="Cargo")
    percoshorcar = models.IntegerField(db_column='PerCosHorCar', blank=True, null=True, verbose_name="Costo por Hora del Cargo")

    class Meta:
        verbose_name = "Personal por Cargo"
        verbose_name_plural = "Personal por Cargos"
        db_table = 'personal_cargos_personal'

    def __str__(self):
        return f"{self.percod} - {self.carpercod}"

class TipoProyecto(models.Model):
    tipprocod = models.AutoField(db_column='TipProCod', primary_key=True, verbose_name="Código")
    tippronom = models.CharField(db_column='TipProNom', max_length=60, verbose_name="Nombre")
    estregcod = models.ForeignKey(EstadoRegistro, on_delete=models.PROTECT, db_column='EstRegCod', verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Tipo de Proyecto"
        verbose_name_plural = "Tipos de Proyecto"
        db_table = 'tipo_proyecto'

    def __str__(self):
        return self.tippronom

class EstadoProyecto(models.Model):
    estprocod = models.AutoField(db_column='EstProCod', primary_key=True, verbose_name="Código")
    estpronom = models.CharField(db_column='EstProNom', max_length=60, verbose_name="Nombre")
    estregcod = models.ForeignKey(EstadoRegistro, on_delete=models.PROTECT, db_column='EstRegCod', verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Estado de Proyecto"
        verbose_name_plural = "Estados de Proyecto"
        db_table = 'estado_proyecto'

    def __str__(self):
        return self.estpronom

class EtapasProyecto(models.Model):
    etaprocod = models.AutoField(db_column='EtaProCod', primary_key=True, verbose_name="Código")
    etapronom = models.CharField(db_column='EtaProNom', max_length=60, verbose_name="Nombre")
    etaprofecreg = models.DateTimeField(db_column='EtaProFecReg', blank=True, null=True, verbose_name="Fecha de Registro")
    etaprofecini = models.DateTimeField(db_column='EtaProFecIni', blank=True, null=True, verbose_name="Fecha de Inicio")
    etaprofecfin = models.DateTimeField(db_column='EtaProFecFin', blank=True, null=True, verbose_name="Fecha de Fin")
    estregcod = models.ForeignKey(EstadoRegistro, on_delete=models.PROTECT, db_column='EstRegCod', verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Etapa de Proyecto"
        verbose_name_plural = "Etapas de Proyecto"
        db_table = 'etapas_proyecto'

    def __str__(self):
        return self.etapronom

class Proyecto(models.Model):
    prosec = models.AutoField(db_column='ProSec', primary_key=True, verbose_name="Código")
    profecprocon = models.DateField(db_column='ProFecProCon', blank=True, null=True, verbose_name="Fecha de Concepción")
    profecpropac = models.DateField(db_column='ProFecProPac', blank=True, null=True, verbose_name="Fecha Pactada")
    profecproini = models.DateField(db_column='ProFecProIni', blank=True, null=True, verbose_name="Fecha de Inicio")
    profecproent = models.DateField(db_column='ProFecProEnt', blank=True, null=True, verbose_name="Fecha de Entrega")
    profecprocie = models.DateField(db_column='ProFecProCie', blank=True, null=True, verbose_name="Fecha de Cierre")
    promonpro = models.DecimalField(db_column='ProMonPro', max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Monto Proyectado")
    promonprorea = models.DecimalField(db_column='ProMonProRea', max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Monto Real")
    promonprocos = models.DecimalField(db_column='ProMonProCos', max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Costo Proyectado")
    promonprocosrea = models.DecimalField(db_column='ProMonProCosRea', max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Costo Real")
    promonprogas = models.DecimalField(db_column='ProMonProGas', max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Gastos Proyectados")
    promonprogasrea = models.DecimalField(db_column='ProMonProGasRea', max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Gastos Reales")
    promonprouti = models.DecimalField(db_column='ProMonProUti', max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Utilidad Proyectada")
    promonproutirea = models.DecimalField(db_column='ProMonProUtiRea', max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Utilidad Real")
    clicod = models.ForeignKey(Cliente, on_delete=models.PROTECT, db_column='CliCod', verbose_name="Cliente")
    proestprocod = models.ForeignKey(EstadoProyecto, on_delete=models.PROTECT, db_column='ProEstProCod', verbose_name="Estado del Proyecto")
    protipprocod = models.ForeignKey(TipoProyecto, on_delete=models.PROTECT, db_column='ProTipProCod', verbose_name="Tipo de Proyecto")
    proetaprocod = models.ForeignKey(EtapasProyecto, on_delete=models.PROTECT, db_column='ProEtaProCod', verbose_name="Etapa del Proyecto")
    estregcod = models.ForeignKey(EstadoRegistro, on_delete=models.PROTECT, db_column='EstRegCod', verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        db_table = 'proyecto'

    def __str__(self):
        return f"Proyecto {self.prosec} - Cliente: {self.clicod}"

class CargosProyecto(models.Model): # listo
    carprocod = models.AutoField(db_column='CarProCod', primary_key=True, verbose_name="Código")
    carpronom = models.CharField(db_column='CarProNom', max_length=60, verbose_name="Nombre")
    prosec = models.ForeignKey(Proyecto, on_delete=models.CASCADE, db_column='ProSec', verbose_name="Proyecto")
    estregcod = models.ForeignKey(EstadoRegistro, on_delete=models.PROTECT, db_column='EstRegCod', verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Cargo de Proyecto"
        verbose_name_plural = "Cargos de Proyecto"
        db_table = 'cargos_proyecto'

    def __str__(self):
        return f"{self.carpronom} - Proyecto: {self.prosec}"

class PersonalCargosProyecto(models.Model):
    percarprocod = models.AutoField(db_column='PerCarProCod', primary_key=True, verbose_name="Código")
    carprocod = models.ForeignKey(CargosProyecto, on_delete=models.CASCADE, db_column='CarProCod', verbose_name="Cargo de Proyecto")
    percod = models.ForeignKey(Personal, on_delete=models.CASCADE, db_column='PerCod', verbose_name="Personal")

    class Meta:
        verbose_name = "Personal por Cargo de Proyecto"
        verbose_name_plural = "Personal por Cargos de Proyecto"
        db_table = 'personal_cargos_proyecto'

    def __str__(self):
        return f"{self.percod} - {self.carprocod}"

class Actividad(models.Model): # listo
    actcod = models.AutoField(db_column='ActCod', primary_key=True, verbose_name="Código")
    actnom = models.CharField(db_column='ActNom', max_length=60, verbose_name="Nombre")
    actfecini = models.DateTimeField(db_column='ActfecIni', blank=True, null=True, verbose_name="Fecha de Inicio")
    actfecfin = models.DateTimeField(db_column='ActFecFin', blank=True, null=True, verbose_name="Fecha de Fin")
    acttip = models.CharField(db_column='ActTip', max_length=20, blank=True, null=True, verbose_name="Tipo")
    acthortradia = models.TimeField(db_column='ActHorTraDia', blank=True, null=True, verbose_name="Horas de Trabajo Diarias")
    estregcod = models.ForeignKey(EstadoRegistro, on_delete=models.PROTECT, db_column='EstRegCod', verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
        db_table = 'actividad'

    def __str__(self):
        return f"{self.actnom} - {self.acttip} - {self.estregcod}"

class PersonalActividad(models.Model):
    peractcod = models.AutoField(db_column='PerActCod', primary_key=True, verbose_name="Código")
    actcod = models.ForeignKey(Actividad, on_delete=models.CASCADE, db_column='ActCod', verbose_name="Actividad")
    percod = models.ForeignKey(Personal, on_delete=models.CASCADE, db_column='PerCod', verbose_name="Personal")

    class Meta:
        verbose_name = "Personal por Actividad"
        verbose_name_plural = "Personal por Actividades"
        db_table = 'personal_actividad'

    def __str__(self):
        return f"{self.percod} - {self.actcod}"

class Complejidad(models.Model): # listo
    comcod = models.AutoField(db_column='ComCod', primary_key=True, verbose_name="Código")
    comnom = models.CharField(db_column='ComNom', max_length=60, verbose_name="Nombre")
    comgra = models.IntegerField(db_column='ComGra', verbose_name="Grado")
    estregcod = models.ForeignKey(EstadoRegistro, on_delete=models.PROTECT, db_column='EstRegCod', verbose_name="Estado de Registro")

    class Meta:
        verbose_name = "Complejidad"
        verbose_name_plural = "Complejidades"
        db_table = 'complejidad'

    def __str__(self):
        return f"{self.comnom} - {self.comgra}"

class ActividadesComplejidad(models.Model): # listo
    actcomcod = models.AutoField(db_column='ActComCod', primary_key=True, verbose_name="Código")
    actcod = models.ForeignKey(Actividad, on_delete=models.CASCADE, db_column='ActCod', verbose_name="Actividad")
    comcod = models.ForeignKey(Complejidad, on_delete=models.CASCADE, db_column='ComCod', verbose_name="Complejidad")

    class Meta:
        verbose_name = "Actividad por Complejidad"
        verbose_name_plural = "Actividades por Complejidad"
        db_table = 'actividades_complejidad'

    def __str__(self):
        return f"{self.actcod} - {self.comcod}"

class EtapaActividad(models.Model):
    etaactcod = models.AutoField(db_column='EtaActCod', primary_key=True, verbose_name="Código")
    actcod = models.ForeignKey(Actividad, on_delete=models.CASCADE, db_column='ActCod', verbose_name="Actividad")
    etaprocod = models.ForeignKey(EtapasProyecto, on_delete=models.CASCADE, db_column='EtaProCod', verbose_name="Etapa del Proyecto")

    class Meta:
        verbose_name = "Etapa de Actividad"
        verbose_name_plural = "Etapas de Actividades"
        db_table = 'etapa_actividad'

    def __str__(self):
        return f"{self.etaprocod} - {self.actcod}"

class Incidencias(models.Model):
    inccod = models.AutoField(db_column='IncCod', primary_key=True, verbose_name="Código")
    incfecini = models.DateTimeField(db_column='IncFecIni', verbose_name="Fecha de Inicio")
    incnom = models.CharField(db_column='IncNom', max_length=60, blank=True, null=True, verbose_name="Nombre")
    incfecfin = models.DateTimeField(db_column='IncFecFin', blank=True, null=True, verbose_name="Fecha de Fin")
    incdes = models.CharField(db_column='IncDes', max_length=255, blank=True, null=True, verbose_name="Descripción")
    actcod = models.ForeignKey(Actividad, on_delete=models.CASCADE, db_column='ActCod', verbose_name="Actividad")

    class Meta:
        verbose_name = "Incidencia"
        verbose_name_plural = "Incidencias"
        db_table = 'incidencias'

    def __str__(self):
        return f"{self.incnom} - {self.actcod}"

class IncidenciaPersonal(models.Model):
    incpercod = models.AutoField(db_column='IncPerCod', primary_key=True, verbose_name="Código")
    inccod = models.ForeignKey(Incidencias, on_delete=models.CASCADE, db_column='IncCod', verbose_name="Incidencia")
    percod = models.ForeignKey(Personal, on_delete=models.CASCADE, db_column='PerCod', verbose_name="Personal")

    class Meta:
        verbose_name = "Incidencia por Personal"
        verbose_name_plural = "Incidencias por Personal"
        db_table = 'incidencia_personal'

    def __str__(self):
        return f"{self.inccod} - {self.percod}"