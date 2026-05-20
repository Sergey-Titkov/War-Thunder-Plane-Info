import war_thunder_plane_info.wt as wt

plane_datamine = wt.WTPlaneFullInfo(plane_id='rafale_c_f3', plane_name = 'plane_names[plane_id]', paths = wt.WTTelemetryPaths(r'e:\git_repo\war_thunder_plane_data\War-Thunder-Datamine-master'))
print(plane_datamine)
