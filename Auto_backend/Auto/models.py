from django.db import models


class Configuration(models.Model):
    id = models.CharField(unique=True, max_length=50, blank=True, null=False, primary_key=True)
    doors_count = models.SmallIntegerField(db_column='doors-count', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    body_type = models.CharField(db_column='body-type', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    configuration_name = models.CharField(db_column='configuration-name', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    generation = models.ForeignKey('Generation', models.DO_NOTHING, blank=True, null=True, related_name='configurations')

    class Meta:
        managed = False
        db_table = 'configuration'


class Generation(models.Model):
    id = models.CharField(unique=True, max_length=50, blank=True, null=False, primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    year_start = models.SmallIntegerField(db_column='year-start', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    year_stop = models.SmallIntegerField(db_column='year-stop', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    is_restyle = models.SmallIntegerField(db_column='is-restyle', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    model = models.ForeignKey('Model', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'generation'


class Mark(models.Model):
    id = models.CharField(unique=True, max_length=50, blank=True, null=False, primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    cyrillic_name = models.CharField(db_column='cyrillic-name', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    popular = models.SmallIntegerField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mark'


class Model(models.Model):
    id = models.CharField(unique=True, max_length=50, blank=True, null=False, primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    cyrillic_name = models.CharField(db_column='cyrillic-name', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    class_field = models.CharField(db_column='class', max_length=5, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    year_from = models.SmallIntegerField(db_column='year-from', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    year_to = models.SmallIntegerField(db_column='year-to', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    mark = models.ForeignKey(Mark, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model'


class Modification(models.Model):
    complectation_id = models.CharField(db_column='complectation-id', unique=True, max_length=50, blank=True, null=False, primary_key=True)  # Field renamed to remove unsuitable characters.
    offers_price_from = models.BigIntegerField(db_column='offers-price-from', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    offers_price_to = models.BigIntegerField(db_column='offers-price-to', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    group_name = models.CharField(db_column='group-name', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    configuration = models.ForeignKey(Configuration, models.DO_NOTHING, blank=True, null=True, related_name='modifications')

    class Meta:
        managed = False
        db_table = 'modification'


class Options(models.Model):
    complectation = models.ForeignKey(Modification, models.DO_NOTHING, blank=True, null=True, related_name='options')
    alcantara = models.CharField(max_length=100, blank=True, null=True)
    black_roof = models.CharField(db_column='black-roof', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    combo_interior = models.CharField(db_column='combo-interior', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    decorative_interior_lighting = models.CharField(db_column='decorative-interior-lighting', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    door_sill_panel = models.CharField(db_column='door-sill-panel', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    driver_seat_electric = models.CharField(db_column='driver-seat-electric', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    driver_seat_memory = models.CharField(db_column='driver-seat-memory', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    driver_seat_support = models.CharField(db_column='driver-seat-support', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    driver_seat_updown = models.CharField(db_column='driver-seat-updown', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    eco_leather = models.CharField(db_column='eco-leather', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    electro_rear_seat = models.CharField(db_column='electro-rear-seat', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    fabric_seats = models.CharField(db_column='fabric-seats', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    folding_front_passenger_seat = models.CharField(db_column='folding-front-passenger-seat', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    folding_tables_rear = models.CharField(db_column='folding-tables-rear', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    front_centre_armrest = models.CharField(db_column='front-centre-armrest', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    front_seat_support = models.CharField(db_column='front-seat-support', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    front_seats_heat = models.CharField(db_column='front-seats-heat', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    front_seats_heat_vent = models.CharField(db_column='front-seats-heat-vent', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hatch = models.CharField(max_length=100, blank=True, null=True)
    leather = models.CharField(max_length=100, blank=True, null=True)
    leather_gear_stick = models.CharField(db_column='leather-gear-stick', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    massage_seats = models.CharField(db_column='massage-seats', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    panorama_roof = models.CharField(db_column='panorama-roof', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    passenger_seat_electric = models.CharField(db_column='passenger-seat-electric', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    passenger_seat_updown = models.CharField(db_column='passenger-seat-updown', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    rear_seat_heat_vent = models.CharField(db_column='rear-seat-heat-vent', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    rear_seat_memory = models.CharField(db_column='rear-seat-memory', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    rear_seats_heat = models.CharField(db_column='rear-seats-heat', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    roller_blind_for_rear_window = models.CharField(db_column='roller-blind-for-rear-window', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    roller_blinds_for_rear_side_windows = models.CharField(db_column='roller-blinds-for-rear-side-windows', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    seat_memory = models.CharField(db_column='seat-memory', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    seat_transformation = models.CharField(db_column='seat-transformation', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sport_pedals = models.CharField(db_column='sport-pedals', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sport_seats = models.CharField(db_column='sport-seats', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    third_rear_headrest = models.CharField(db_column='third-rear-headrest', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    third_row_seats = models.CharField(db_column='third-row-seats', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tinted_glass = models.CharField(db_column='tinted-glass', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    wheel_heat = models.CharField(db_column='wheel-heat', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    wheel_leather = models.CharField(db_column='wheel-leather', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    number_360_camera = models.CharField(db_column='360-camera', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    adj_pedals = models.CharField(db_column='adj-pedals', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ashtray_and_cigarette_lighter = models.CharField(db_column='ashtray-and-cigarette-lighter', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    auto_cruise = models.CharField(db_column='auto-cruise', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    auto_mirrors = models.CharField(db_column='auto-mirrors', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    auto_park = models.CharField(db_column='auto-park', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    climate_control_1 = models.CharField(db_column='climate-control-1', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    climate_control_2 = models.CharField(db_column='climate-control-2', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    computer = models.CharField(max_length=100, blank=True, null=True)
    condition = models.CharField(max_length=100, blank=True, null=True)
    cooling_box = models.CharField(db_column='cooling-box', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cruise_control = models.CharField(db_column='cruise-control', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    drive_mode_sys = models.CharField(db_column='drive-mode-sys', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    e_adjustment_wheel = models.CharField(db_column='e-adjustment-wheel', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    easy_trunk_opening = models.CharField(db_column='easy-trunk-opening', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    electro_mirrors = models.CharField(db_column='electro-mirrors', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    electro_trunk = models.CharField(db_column='electro-trunk', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    electro_window_back = models.CharField(db_column='electro-window-back', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    electro_window_front = models.CharField(db_column='electro-window-front', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    electronic_gage_panel = models.CharField(db_column='electronic-gage-panel', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    front_camera = models.CharField(db_column='front-camera', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    keyless_entry = models.CharField(db_column='keyless-entry', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    multi_wheel = models.CharField(db_column='multi-wheel', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    multizone_climate_control = models.CharField(db_column='multizone-climate-control', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    park_assist_f = models.CharField(db_column='park-assist-f', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    park_assist_r = models.CharField(db_column='park-assist-r', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    power_latching_doors = models.CharField(db_column='power-latching-doors', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    programmed_block_heater = models.CharField(db_column='programmed-block-heater', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    projection_display = models.CharField(db_column='projection-display', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    rear_camera = models.CharField(db_column='rear-camera', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    remote_engine_start = models.CharField(db_column='remote-engine-start', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    servo = models.CharField(max_length=100, blank=True, null=True)
    start_button = models.CharField(db_column='start-button', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    start_stop_function = models.CharField(db_column='start-stop-function', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    steering_wheel_gear_shift_paddles = models.CharField(db_column='steering-wheel-gear-shift-paddles', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    wheel_configuration1 = models.CharField(db_column='wheel-configuration1', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    wheel_configuration2 = models.CharField(db_column='wheel-configuration2', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    wheel_memory = models.CharField(db_column='wheel-memory', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    wheel_power = models.CharField(db_column='wheel-power', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    adaptive_light = models.CharField(db_column='adaptive-light', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    automatic_lighting_control = models.CharField(db_column='automatic-lighting-control', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    drl = models.CharField(max_length=100, blank=True, null=True)
    heated_wash_system = models.CharField(db_column='heated-wash-system', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    high_beam_assist = models.CharField(db_column='high-beam-assist', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    laser_lights = models.CharField(db_column='laser-lights', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    led_lights = models.CharField(db_column='led-lights', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    light_cleaner = models.CharField(db_column='light-cleaner', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    light_sensor = models.CharField(db_column='light-sensor', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    mirrors_heat = models.CharField(db_column='mirrors-heat', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ptf = models.CharField(max_length=100, blank=True, null=True)
    rain_sensor = models.CharField(db_column='rain-sensor', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    windcleaner_heat = models.CharField(db_column='windcleaner-heat', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    windscreen_heat = models.CharField(db_column='windscreen-heat', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xenon = models.CharField(max_length=100, blank=True, null=True)
    abs = models.CharField(max_length=100, blank=True, null=True)
    airbag_curtain = models.CharField(db_column='airbag-curtain', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    airbag_driver = models.CharField(db_column='airbag-driver', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    airbag_passenger = models.CharField(db_column='airbag-passenger', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    airbag_rear_side = models.CharField(db_column='airbag-rear-side', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    airbag_side = models.CharField(db_column='airbag-side', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    asr = models.CharField(max_length=100, blank=True, null=True)
    bas = models.CharField(max_length=100, blank=True, null=True)
    blind_spot = models.CharField(db_column='blind-spot', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    collision_prevention_assist = models.CharField(db_column='collision-prevention-assist', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    dha = models.CharField(max_length=100, blank=True, null=True)
    drowsy_driver_alert_system = models.CharField(db_column='drowsy-driver-alert-system', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    esp = models.CharField(max_length=100, blank=True, null=True)
    feedback_alarm = models.CharField(db_column='feedback-alarm', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    glonass = models.CharField(max_length=100, blank=True, null=True)
    hcc = models.CharField(max_length=100, blank=True, null=True)
    isofix = models.CharField(max_length=100, blank=True, null=True)
    isofix_front = models.CharField(db_column='isofix-front', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    knee_airbag = models.CharField(db_column='knee-airbag', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    laminated_safety_glass = models.CharField(db_column='laminated-safety-glass', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    lane_keeping_assist = models.CharField(db_column='lane-keeping-assist', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    night_vision = models.CharField(db_column='night-vision', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    power_child_locks_rear_doors = models.CharField(db_column='power-child-locks-rear-doors', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    traffic_sign_recognition = models.CharField(db_column='traffic-sign-recognition', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tyre_pressure = models.CharField(db_column='tyre-pressure', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    vsm = models.CharField(max_length=100, blank=True, null=True)
    alarm = models.CharField(max_length=100, blank=True, null=True)
    immo = models.CharField(max_length=100, blank=True, null=True)
    lock = models.CharField(max_length=100, blank=True, null=True)
    volume_sensor = models.CharField(db_column='volume-sensor', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    number_12v_socket = models.CharField(db_column='12v-socket', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_220v_socket = models.CharField(db_column='220v-socket', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    android_auto = models.CharField(db_column='android-auto', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    apple_carplay = models.CharField(db_column='apple-carplay', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    audiopreparation = models.CharField(max_length=100, blank=True, null=True)
    audiosystem_cd = models.CharField(db_column='audiosystem-cd', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    audiosystem_tv = models.CharField(db_column='audiosystem-tv', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    aux = models.CharField(max_length=100, blank=True, null=True)
    bluetooth = models.CharField(max_length=100, blank=True, null=True)
    entertainment_system_for_rear_seat_passengers = models.CharField(db_column='entertainment-system-for-rear-seat-passengers', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    music_super = models.CharField(db_column='music-super', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    navigation = models.CharField(max_length=100, blank=True, null=True)
    usb = models.CharField(max_length=100, blank=True, null=True)
    voice_recognition = models.CharField(db_column='voice-recognition', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    wireless_charger = models.CharField(db_column='wireless-charger', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    ya_auto = models.CharField(db_column='ya-auto', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    activ_suspension = models.CharField(db_column='activ-suspension', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    air_suspension = models.CharField(db_column='air-suspension', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    reduce_spare_wheel = models.CharField(db_column='reduce-spare-wheel', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    spare_wheel = models.CharField(db_column='spare-wheel', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sport_suspension = models.CharField(db_column='sport-suspension', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    number_14_inch_wheels = models.CharField(db_column='14-inch-wheels', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_15_inch_wheels = models.CharField(db_column='15-inch-wheels', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_16_inch_wheels = models.CharField(db_column='16-inch-wheels', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_17_inch_wheels = models.CharField(db_column='17-inch-wheels', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_18_inch_wheels = models.CharField(db_column='18-inch-wheels', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_19_inch_wheels = models.CharField(db_column='19-inch-wheels', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_20_inch_wheels = models.CharField(db_column='20-inch-wheels', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_21_inch_wheels = models.CharField(db_column='21-inch-wheels', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    number_22_inch_wheels = models.CharField(db_column='22-inch-wheels', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    body_kit = models.CharField(db_column='body-kit', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    body_mouldings = models.CharField(db_column='body-mouldings', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    duo_body_color = models.CharField(db_column='duo-body-color', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    paint_metallic = models.CharField(db_column='paint-metallic', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    roof_rails = models.CharField(db_column='roof-rails', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    steel_wheels = models.CharField(db_column='steel-wheels', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'options'


class Specifications(models.Model):
    complectation = models.ForeignKey(Modification, models.DO_NOTHING, blank=True, null=True, related_name='specifications')
    back_brake = models.CharField(db_column='back-brake', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    feeding = models.CharField(max_length=100, blank=True, null=True)
    horse_power = models.CharField(db_column='horse-power', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    kvt_power = models.CharField(db_column='kvt-power', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    rpm_power = models.CharField(db_column='rpm-power', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    engine_type = models.CharField(db_column='engine-type', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    transmission = models.CharField(max_length=100, blank=True, null=True)
    drive = models.CharField(max_length=100, blank=True, null=True)
    volume = models.CharField(max_length=100, blank=True, null=True)
    time_to_100 = models.CharField(db_column='time-to-100', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cylinders_order = models.CharField(db_column='cylinders-order', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    max_speed = models.CharField(db_column='max-speed', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    compression = models.CharField(max_length=100, blank=True, null=True)
    cylinders_value = models.CharField(db_column='cylinders-value', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    diametr = models.CharField(max_length=100, blank=True, null=True)
    piston_stroke = models.CharField(db_column='piston-stroke', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    engine_feeding = models.CharField(db_column='engine-feeding', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    engine_order = models.CharField(db_column='engine-order', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    gear_value = models.CharField(db_column='gear-value', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    moment = models.CharField(max_length=100, blank=True, null=True)
    petrol_type = models.CharField(db_column='petrol-type', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    valves = models.CharField(max_length=100, blank=True, null=True)
    weight = models.CharField(max_length=100, blank=True, null=True)
    wheel_size = models.CharField(db_column='wheel-size', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    wheel_base = models.CharField(db_column='wheel-base', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    front_wheel_base = models.CharField(db_column='front-wheel-base', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    back_wheel_base = models.CharField(db_column='back-wheel-base', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    front_brake = models.CharField(db_column='front-brake', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    front_suspension = models.CharField(db_column='front-suspension', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    back_suspension = models.CharField(db_column='back-suspension', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    height = models.CharField(max_length=100, blank=True, null=True)
    width = models.CharField(max_length=100, blank=True, null=True)
    fuel_tank_capacity = models.CharField(db_column='fuel-tank-capacity', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    seats = models.CharField(max_length=100, blank=True, null=True)
    length = models.CharField(max_length=100, blank=True, null=True)
    emission_euro_class = models.CharField(db_column='emission-euro-class', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    volume_litres = models.CharField(db_column='volume-litres', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    consumption_mixed = models.CharField(db_column='consumption-mixed', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    clearance = models.CharField(max_length=100, blank=True, null=True)
    trunks_min_capacity = models.CharField(db_column='trunks-min-capacity', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    trunks_max_capacity = models.CharField(db_column='trunks-max-capacity', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    consumption_hiway = models.CharField(db_column='consumption-hiway', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    consumption_city = models.CharField(db_column='consumption-city', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    moment_rpm = models.CharField(db_column='moment-rpm', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    full_weight = models.CharField(db_column='full-weight', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    range_distance = models.CharField(db_column='range-distance', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    battery_capacity = models.CharField(db_column='battery-capacity', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    fuel_emission = models.CharField(db_column='fuel-emission', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    electric_range = models.CharField(db_column='electric-range', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    charge_time = models.CharField(db_column='charge-time', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    safety_rating = models.CharField(db_column='safety-rating', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    safety_grade = models.CharField(db_column='safety-grade', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'specifications'
