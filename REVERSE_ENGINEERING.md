# myenergi API reverse engineering notes

## Zappi

### `/cgi-zappi-mode`

Control Zappi charge modes (Fast, Eco, Eco+, Stop).
Control Zappi Manual Boost and Smart Boost configuration.

#### Observed requests

- Fast `/cgi-zappi-mode-Z{serial}-1-0-0-0000`
- Eco `/cgi-zappi-mode-Z{serial}-2-0-0-0000`
- Eco+ `/cgi-zappi-mode-Z{serial}-3-0-0-0000`
- Stop `/cgi-zappi-mode-Z{serial}-4-0-0-0000`
- Eco+, + Smart Boost, 01:15am, 40kWh: `/cgi-zappi-mode-Z{serial}-0-11-40-0115`
- Stop Smart Boost: `/cgi-zappi-mode-Z{serial}-0-2-0-0000`
- Eco+, + Manual Boost, 10kWh: `/cgi-zappi-mode-Z{serial}-0-10-10-0000`
- Stop Manual Boost: `/cgi-zappi-mode-Z{serial}-0-2-0-0000`

#### Inferred general form

`/cgi-zappi-mode-Z{serial}-{charge_mode}-{boost_mode}-{charge_kwh}-{charge_by}`, where:

- `serial`: Zappi serial number
- `charge_mode`: Charge mode
  - `0`: Change boost mode, mot charge mode.
  - `1`: Fast
  - `2`: Eco
  - `3`: Eco+
  - `4`: Stop
- `boost_mode`: Boost mode
  - `2`: Stop boost
  - `10`: Manual boost
  - `11`: Smart boost
- `charge_kwh`: Energy to add boost (in kWh).
  - Presumably, only values selectable in the app are allowed (`5`, `10`, `20`, `40`, `60`, `80`, `100`).
  - `0` when stopping boost or changing general charge mode.
- `charge_by`: Time to finish Smart Boost before (in HHMM format, e.g. `0115` for 01:15am).
  - `0000` when stopping boost or changing general charge mode.
