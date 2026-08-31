# ALPSTUGA ventilation blueprints for Home Assistant

Safe, reusable Home Assistant blueprints derived from a real installation that
uses an IKEA ALPSTUGA air-quality monitor to request a bounded ventilation
Boost from Swegon CASA.

Blueprint input names and safety descriptions are shown in both Norwegian
Bokmål and English. Runtime mode values are language-neutral, so the same
automation works regardless of the Home Assistant UI language.

The first blueprint is vendor-flexible: it works with an ALPSTUGA connected over
Matter and any ventilation integration that exposes its operating mode as a
Home Assistant `select` entity.

## Air-quality ventilation boost

[![Open your Home Assistant instance and show the blueprint import dialog.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fkennethaasan%2Fha-alpstuga-swegon-blueprints%2Fblob%2Fmain%2Fblueprints%2Fautomation%2Fkennethaasan%2Falpstuga_ventilation_boost.yaml)

The automation:

- starts only after sustained high CO2 or humidity, or an optional sustained
  predictive demand sensor;
- refuses to start when PM2.5 is unsafe or required sensor data is unavailable;
- can require optional binary safety entities for alarms, telemetry freshness,
  or a master enable switch;
- only takes ownership from configured normal modes;
- remembers and restores the previous normal mode;
- persists ownership, the previous mode, and the hard deadline across Home
  Assistant restarts;
- stops after sustained recovery, unsafe PM2.5, a manual mode change, or a
  configurable hard time limit; and
- never restores over a later manual mode change.

Recommended defaults are 1000/800 ppm CO2, 65/60% relative humidity, a PM2.5
limit of 25 µg/m³, and a two-hour maximum Boost.

Predictive demand is optional. A useful implementation combines the current
CO2 level with a smoothed rate of rise and turns on only when a bounded forecast
crosses the normal start threshold. The blueprint treats that input only as a
demand signal: every existing safety gate, eligible-mode check, recovery rule,
manual override, and maximum-duration limit remains authoritative.

### Moisture-aware humidity demand

Relative humidity alone does not say whether outdoor air can dry a building.
Installations with indoor/outdoor temperature and humidity can calculate
absolute humidity in `g/m³`, then expose a template humidity sensor that mirrors
the real indoor relative humidity only while outdoor air is meaningfully drier
(for example by at least `0.3 g/m³`) and reports `0` otherwise. Select that
template as the blueprint's humidity sensor. CO2 demand remains independent
because it uses its own input.

A separate binary sensor can detect a sustained humidity rate of rise—for
example at least 12 percentage points/hour while indoor RH is at least 50% and
outdoor air is drier—and be added under **Predictive demand sensors**. This can
react to showers or cooking before the fixed high-humidity threshold, while the
blueprint still enforces PM2.5, telemetry, alarm, ownership, recovery, manual
override, and maximum-duration safeguards.

## Requirements

- Home Assistant 2024.10 or newer
- an ALPSTUGA—or equivalent—CO2, humidity and PM2.5 sensor
- a ventilation integration with a writable mode `select`
- one `input_boolean` ownership helper, one `input_select` whose options cover
  the eligible/fallback modes, and one `timer` helper with restore enabled

The helpers make restart behavior explicit: an in-progress automation-owned
Boost continues after a normal Home Assistant restart, while its original hard
deadline and previous mode remain intact. A mode changed while Home Assistant
was offline is treated as a manual override and is never overwritten.
Integrations that report a read-only `Automatic` state can list it as eligible
while excluding it from **Writable modes that can be restored**; the blueprint
then restores the configured fallback such as `Home`.

The blueprint does not alter commissioning parameters, fan calibration, heater
settings, alarms, or physical safety controls.

## Upgrading from 1.x

Version 2 requires three persistent Home Assistant helpers for each automation:

- an `input_boolean` that records Boost ownership;
- an `input_select` containing the normal/fallback ventilation modes; and
- a `timer` configured with restore enabled.

Open the imported blueprint automation after updating, select those helpers,
and save it. If the integration reports a read-only state such as `Automatic`,
include it under eligible modes but omit it from writable restore modes; set
`Home` as the fallback.

## Release policy

Every functional change is versioned and published as a GitHub release. Stable
deployments should pin a release tag rather than consume the moving `main`
branch. Breaking blueprint-input changes increment the major version.

## Important limitations

This project cannot rotate the physical ALPSTUGA display. IKEA currently exposes
display power but not display-page selection over Matter. The requested upstream
solution is a Matter Mode Select cluster for CO2, PM2.5, temperature, humidity
and clock pages.

## License

Apache-2.0. See [LICENSE](LICENSE).
