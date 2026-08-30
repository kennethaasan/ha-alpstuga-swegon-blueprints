# Changelog

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
