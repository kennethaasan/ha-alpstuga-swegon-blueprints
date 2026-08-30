# Changelog

## 2.2.0 - 2026-08-30

- Add Norwegian Bokmål alongside English to every blueprint input, safety
  description, and trace stop reason.
- Use language-neutral Swegon mode values compatible with localized versions of
  `ha-swegon-casa-cloud` 0.5.0 and newer.

## 2.1.0 - 2026-08-30

- Accept optional predictive binary demand sensors, such as a bounded CO2
  rate-of-rise forecast, without bypassing PM2.5, telemetry, alarm, ownership,
  mode, recovery, or maximum-duration safeguards.
- Allow a separate sustained duration for predictive demand.

## 2.0.0 - 2026-08-30

- Preserve automation ownership, the previous ventilation mode, and the hard
  Boost deadline across Home Assistant restarts.
- Respect a ventilation mode changed while Home Assistant was offline.
- Separate eligible modes from writable restore modes so integrations may
  report a read-only `Automatic` state and safely restore `Home`.
- Require an `input_boolean`, `input_select`, and restore-enabled `timer` helper
  when creating the automation from the blueprint.

## 1.1.0 - 2026-08-30

- Add optional binary safety gates and a sustained safety-failure duration.

## 1.0.0 - 2026-08-30

- Initial bounded CO2/humidity ventilation Boost blueprint.
