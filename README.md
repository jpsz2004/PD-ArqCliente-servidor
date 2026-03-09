# Preguntas de Reflexión

## ¿Qué problema resuelve Singleton aquí?

El patrón **Singleton** se utiliza en la clase `MonitoringConfig` para garantizar que exista **una única instancia de configuración global** en todo el sistema.

En el sistema de monitoreo, diferentes componentes necesitan acceder a los **umbrales de métricas**, por ejemplo el límite permitido de CPU. Si cada componente tuviera su propia instancia de configuración, podrían existir inconsistencias entre los valores utilizados para evaluar el estado del sistema.

Singleton resuelve este problema al asegurar que:

- Solo exista una instancia de configuración.
- Todos los componentes utilicen los mismos valores.
- Cualquier cambio en la configuración se refleje globalmente.

En nuestra implementación, `MonitoringFacade` consulta el umbral de CPU a través de `MonitoringConfig`, y al ser Singleton se garantiza que siempre se utilice la misma configuración en todo el sistema.

---

## ¿Cómo desacoplar servicios externos?

Los servicios externos se desacoplan mediante el uso del patrón **Adapter**, implementado en la clase `LegacyAdapter`.

La API externa (`LegacyAPI`) devuelve los datos en un formato diferente al modelo interno del sistema, por ejemplo:

```json
{"cpu_usage_percent": 85.0}
```

## ¿Cómo escalar el sistema a 100 microservicios?

El sistema puede escalarse para monitorear múltiples microservicios ampliando la fachada y utilizando múltiples adaptadores o fuentes de métricas.

Una estrategia sería:

- Mantener una colección de servicios o adaptadores dentro de `MonitoringFacade`.
- Ejecutar el monitoreo para cada servicio de forma iterativa.
- Generar alertas de manera independiente para cada microservicio.

Por ejemplo:

```python
for adapter in adapters:
    metric = adapter.get_metric()
```

Gracias al uso del patrón **Adapter**, cada microservicio podría tener su propio adaptador para obtener métricas desde diferentes fuentes sin afectar la lógica central del sistema.

Además, el patrón **Observer** permite que múltiples sistemas de notificación (correo, Slack, SMS, etc.) reciban alertas sin modificar la lógica del monitoreo.

Esto permite que el sistema crezca en cantidad de microservicios manteniendo un bajo nivel de acoplamiento entre los componentes.

---

## ¿Dónde se produciría alto acoplamiento si no se aplican patrones?

Sin el uso de los patrones de diseño aplicados en este proyecto, el sistema presentaría varios puntos de **alto acoplamiento**.

### Integración con servicios externos

Sin el patrón **Adapter**, el sistema dependería directamente del formato de la API externa:

```python
data["cpu_usage_percent"]
```

Si la estructura de la API cambiara, sería necesario modificar múltiples partes del sistema.

---

### Configuración del sistema

Sin el patrón **Singleton**, diferentes partes del sistema podrían crear instancias independientes de configuración, generando inconsistencias en los umbrales o parámetros del monitoreo.

---

### Sistema de notificaciones

Sin el patrón **Observer**, el sistema de monitoreo tendría que llamar directamente a cada mecanismo de notificación:

```python
send_email()
send_slack()
send_sms()
```

Esto haría que la lógica de monitoreo estuviera fuertemente acoplada a los canales de notificación.

---

### Uso del sistema

Sin el patrón **Facade**, el cliente del sistema tendría que interactuar con múltiples clases y coordinar manualmente la lógica de monitoreo, aumentando la complejidad y dificultando el mantenimiento del código.

---

## ¿Por qué Facade mejora la mantenibilidad?

El patrón **Facade** mejora la mantenibilidad porque proporciona una **interfaz única y simplificada** para interactuar con el sistema.

En lugar de que el cliente tenga que coordinar múltiples componentes como:

- `LegacyAPI`
- `LegacyAdapter`
- `MonitoringConfig`
- `AlertObserver`
- creación de `Alert`

el cliente solo necesita interactuar con la clase `MonitoringFacade`.

Por ejemplo:

```python
facade.check_system()
```

Esto reduce la complejidad del código cliente y permite que los detalles internos del sistema cambien sin afectar a quienes lo utilizan.

Además, al centralizar la lógica de coordinación en una sola clase, el sistema se vuelve más fácil de modificar, extender y mantener.