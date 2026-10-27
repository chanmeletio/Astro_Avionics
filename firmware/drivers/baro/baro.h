/**
  ******************************************************************************
  * @file    baro.h
  * @brief   Barometer / Altimeter Driver (MS5611 / BMP390)
  ******************************************************************************
  */

#ifndef DRIVER_BARO_H
#define DRIVER_BARO_H

#include <stdint.h>
#include <stdbool.h>

typedef struct {
    float pressure_pa;      /* Atmospheric pressure in Pascals */
    float temperature_c;    /* Temperature in Celsius */
    float altitude_agl_m;   /* Altitude Above Ground Level in meters */
} baro_data_t;

bool baro_init(void);
void baro_set_ground_reference(float pressure_pa);
bool baro_read(baro_data_t *data);
float baro_pressure_to_altitude(float pressure_pa, float ground_pressure_pa);

#endif /* DRIVER_BARO_H */
