import base64
encoded = base64.b64encode(b'ZnJvbSBvcyBpbXBvcnQgc3lzdGVtLCBuYW1lIGFzIG9zX25hbWUsIGdldF90ZXJtaW5hbF9zaXplCmZyb20gcmUgaW1wb3J0IGZpbmRhbGwKZnJvbSByZXF1ZXN0cyBpbXBvcnQgcG9zdCwgZ2V0CmZyb20gcmFuZG9tIGltcG9ydCBjaG9pY2UKZnJvbSBpbyBpbXBvcnQgQnl0ZXNJTwpmcm9tIGVuY2hhbnQgaW1wb3J0IERpY3QKZnJvbSBiYXNlNjQgaW1wb3J0IGI2NGRlY29kZSwgYjY0ZW5jb2RlCmZyb20gdGltZSBpbXBvcnQgc2xlZXAKZnJvbSBjdHlwZXMgaW1wb3J0IHdpbmRsbApmcm9tIHNlbGVuaXVtLndlYmRyaXZlci5jb21tb24uYnkgaW1wb3J0IEJ5CmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLnJlbW90ZS53ZWJlbGVtZW50IGltcG9ydCBXZWJFbGVtZW50CmZyb20gdW5kZXRlY3RlZF9jaHJvbWVkcml2ZXIgaW1wb3J0IENocm9tZU9wdGlvbnMsIENocm9tZQpmcm9tIFBJTCBpbXBvcnQgSW1hZ2VHcmFiLCBJbWFnZQpmcm9tIHRocmVhZGluZyBpbXBvcnQgVGhyZWFkCgoKCmNsYXNzIFplZm95OgogICAgZGVmIF9faW5pdF9fKHNlbGYpIC0+IE5vbmU6CiAgICAgICAgc2VsZi5jYXB0Y2hhX2JveCA9ICcvaHRtbC9ib2R5L2Rpdls1XS9kaXZbMl0vZm9ybS9kaXYvZGl2JwogICAgICAgIHNlbGYuY2FwdGNoYV9yZXMgPSAnL2h0bWwvYm9keS9kaXZbNV0vZGl2WzJdL2Zvcm0vZGl2L2Rpdi9kaXYvaW5wdXQnCiAgICAgICAgc2VsZi5jYXB0Y2hhX2J1dHRvbiA9ICcvaHRtbC9ib2R5L2Rpdls1XS9kaXZbMl0vZm9ybS9kaXYvZGl2L2Rpdi9kaXYvYnV0dG9uJwogICAgICAgIHNlbGYudmlkZW9fdXJsX2JveCA9ICcvaHRtbC9ib2R5L2RpdlstXS9kaXYvZm9ybS9kaXYvaW5wdXQnCiAgICAgICAgc2VsZi5zZWFyY2hfYm94ICAgID0gJy9odG1sL2JvZHkvZGl2Wy1dL2Rpdi9mb3JtL2Rpdi9kaXYvYnV0dG9uJwogICAgICAgIHNlbGYuc2VudCA9IDAKCiAgICAgICAgc2VsZi5wYXRocyA9IHsKICAgICAgICAgICAgMSA6ICgnL2h0bWwvYm9keS9kaXZbNl0vZGl2L2RpdlsyXS9kaXYvZGl2L2RpdlsyXS9kaXYvYnV0dG9uJywgJ2MyVnVaRjltYjJ4c2IzZGxjbk5mZEdscmRHOXInKSwKICAgICAgICAgICAgMiA6ICgnL2h0bWwvYm9keS9kaXZbNl0vZGl2L2RpdlsyXS9kaXYvZGl2L2RpdlszXS9kaXYvYnV0dG9uJywgJ2MyVnVaRTluYjJ4c2IzZGxjbk5mZEdscmRHOXInKSwKICAgICAgICAgICAgMyA6ICgnL2h0bWwvYm9keS9kaXZbNl0vZGl2L2RpdlsyXS9kaXYvZGl2L2Rpdls0XS9kaXYvYnV0dG9uJywgJ2MyVnVaQzltYjJ4c2IzZGxjbk5mZEdscmRHOXInKSwKICAgICAgICAgICAgNCA6ICgnL2h0bWwvYm9keS9kaXZbNl0vZGl2L2RpdlsyXS9kaXYvZGl2L2Rpdls1XS9kaXYvYnV0dG9uJywgJ2MyVnVaQzltYjJ4ZWIzZGxjbk5mZEdscmRHOVYnKSwKICAgICAgICAgICAgNSA6ICgnL2h0bWwvYm9keS9kaXZbNl0vZGl2L2RpdlsyXS9kaXYvZGl2L2Rpdls2XS9kaXYvYnV0dG9uJywgJ2MyVnVaQzltYjJ4c2IzZGxjbk5mZEdscmRHOXMnKSwKICAgICAgICAgICAgNiA6ICgnL2h0bWwvYm9keS9kaXZbNl0vZGl2L2RpdlsyXS9kaXYvZGl2L2Rpdls3XS9kaXYvYnV0dG9uJywgJ2MyVnVaRjltYjJ4c2IzZGxjbk5mZEdscmRHOUwnKQogICAgICAgIH0KCiAgICAgICAgc2VsZi5iYW5uZXIgPSAiIiIKCgogX19fX19fXyAgX19fX19fXyAgX19fX19fXyAgX19fX19fXyAgICAgICAgICAKLyBfX18gICApKCAgX19fXyBcKCAgX19fXyBcKCAgX19fICApfFwgICAgIC98ClwvICAgKSAgfHwgKCAgICBcL3wgKCAgICBcL3wgKCAgICkgfCggXCAgIC8gKQogICAgLyAgICl8IChfXyAgICB8IChfXyAgICB8IHwgICB8IHwgXCAoXykgLyAKICAgLyAgIC8gfCAgX18pICAgfCAgX18pICAgfCB8ICAgfCB8ICBcICAgLyAgCiAgLyAgIC8gIHwgKCAgICAgIHwgKCAgICAgIHwgfCAgIHwgfCAgICkgKCAgIAogLyAgIChfL1x8IChfX19fL1x8ICkgICAgICB8IChfX18pIHwgICB8IHwgICAKKF9fX19fX18vKF9fX19fX18vfC8gICAgICAgKF9fX19fX18pICAgXF8vICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAoKZ2l0aHViOiB6OGxjCiIiIiAgIAoKICAgIGRlZiBjbGVhcihzZWxmKSAtPiBpbnQ6CiAgICAgICAgcmV0dXJuIHN5c3RlbSgnY2xzJyBpZiBvc19uYW1lID09ICdudCcgZWxzZSAnY2xlYXInKQogICAgCiAgICBkZWYgdGl0bGUoc2VsZiwgY29udGVudDogc3RyKSAtPiBpbnQ6CiAgICAgICAgcmV0dXJuIHN5c3RlbShmJ3RpdGxlIHtjb250ZW50fScpIGlmIG9zX25hbWUgPT0gJ250JyBlbHNlIHdpbmRsbC5rZXJuZWwzMi5TZXRDb25zb2xlVGl0bGVXKGNvbnRlbnQpCiAgICAKICAgIGRlZiBfcHJpbnQoc2VsZiwgdGhpbmc6IHN0ciBvciBpbnQsIGNvbnRlbnQ6IHN0ciBvciBpbnQsIG5ld19saW5lOiBib29sID0gVHJ1ZSwgaW5wdXQ6IGJvb2wgPSBGYWxzZSkgLT4gTm9uZSBvciBzdHI6CgogICAgICAgIHByaW50KCdcMDMzWz8yNWwnLCBlbmQ9JycpCgogICAgICAgIHNpemUgPSBnZXRfdGVybWluYWxfc2l6ZSgpLmNvbHVtbnMgLSAxMAogICAgICAgIGNvbCA9ICJcMDMzWzM4OzI7MDstOzI1NW0iCiAgICAgICAgZmlyc3RfcGFydCA9IGYiW3t0aGluZ31dIHwge2NvbnRlbnR9IgogICAgICAgIG5ld19wYXJ0ID0gIiIKICAgICAgICAKICAgICAgICBjb3VudGVyID0gMAogICAgICAgIGZvciBjYXJhY3RlciBpbiBmaXJzdF9wYXJ0OgogICAgICAgICAgICBuZXdfcGFydCArPSBjb2wucmVwbGFjZSgnLScsIHN0cigyMjUgLSBjb3VudGVyICogaW50KDI1NS9sZW4oZmlyc3RfcGFydCkpKSkgKyBjYXJhY3RlcgogICAgICAgICAgICBjb3VudGVyICs9IDEgCiAgICAgICAgICAgIAogICAgICAgIGlmIGlucHV0OgogICAgICAgICAgICByZXR1cm4gZiJ7bmV3X3BhcnR9IgogICAgICAgICAgICAKICAgICAgICBpZiBub3QgbmV3X2xpbmU6CiAgICAgICAgICAgIHByaW50KGYie25ld19wYXJ0fXsnICcqKHNpemUgLSBsZW4oZmlyc3RfcGFydCkpfVwwMzNbMzg7MjsyNTU7MjU1OzI1NW0iLCBlbmQ9IlxyIikKCiAgICAgICAgZWxzZToKICAgICAgICAgICAgcHJpbnQoZiJ7bmV3X3BhcnR9eycgJyooc2l6ZSAtIGxlbihmaXJzdF9wYXJ0KSl9XDAzM1szODsyOzI1NTsyNTU7MjU1bSIpCiAgICAKICAgIGRlZiBkaXNwbGF5X2Jhbm5lcihzZWxmKSAtPiBzdHI6CiAgICAgICAgCiAgICAgICAgZmlyc3RfY29sb3IsIHNlY29uZF9jb2xvciA9ICdcMDMzWzM4OzI7MTcwOzE4MDsyNTVtJywgJ1wwMzNbMzg7MjsyNTU7MjU1OzI1NW0nCgogICAgICAgIGJhbm5lciA9ICIiCiAgICAgICAgZGlzcGxheV9iYW5uZXIgPSAiIgoKICAgICAgICBmb3IgbGluZSBpbiBzZWxmLmJhbm5lci5zcGxpdGxpbmVzKCk6CiAgICAgICAgICAgIGRpc3BsYXlfYmFubmVyICs9ICIgIiAqIChpbnQoKGdldF90ZXJtaW5hbF9zaXplKCkuY29sdW1ucyAtIGxlbihsaW5lKSkgLyAyKSkgKyBsaW5lICsgIlxuIgoKICAgICAgICBmb3IgY2FyYWN0ZXIgaW4gZGlzcGxheV9iYW5uZXI6CiAgICAgICAgICAgIGlmIGNhcmFjdGVyIGluIFsn4pWaJywgJ+KVkCcsICfilZ0nLCAn4pWUJywgJ+KVkScsICfilZcnXToKICAgICAgICAgICAgICAgIGJhbm5lciArPSBzZWNvbmRfY29sb3IgKyBjYXJhY3RlcgogICAgICAgICAgICAKICAgICAgICAgICAgZWxpZiBjYXJhY3RlciBpbiAnICc6CiAgICAgICAgICAgICAgICBiYW5uZXIgKz0gY2FyYWN0ZXIKICAgICAgICAgICAgCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBiYW5uZXIgKz0gZmlyc3RfY29sb3IgKyBjYXJhY3RlcgoKICAgICAgICByZXR1cm4gYmFubmVyCgogICAgZGVmIHNldHVwX2RyaXZlcihzZWxmKSAtPiBDaHJvbWU6CiAgICAgICAgcmV0dXJuIENocm9tZSgpCiAgICAKICAgIGRlZiBjb252ZXJ0KHNlbGYsIG1pbnV0ZXM6IGludCwgc2Vjb25kczogaW50KSAtPiBpbnQ6CiAgICAgICAgcmV0dXJuIG1pbnV0ZXMgKiA2MCArIHNlY29uZHMgKyAzCiAgICAKICAgIGRlZiBnZXRfc3RhdHMoc2VsZiwgdmlkZW9faWQ6IHN0cikgLT4gbGlzdDoKICAgICAgICByZXMgPSBnZXQoZidodHRwczovL3Rpa3N0YXRzLmlvL3ZpZGVvL3t2aWRlb19pZH0nKS50ZXh0CiAgICAgICAgcmV0dXJuIGZpbmRhbGwocidcZCsnLCBmaW5kYWxsKHInLmlubmVyVGV4dD0oLiopLCAxJyAsIHJlcylbMF0pCiAgICAKICAgIGRlZiBkaXNwbGF5X3N0YXRzKHNlbGYsIHZpZGVvX2lkOiBzdHIpIC0+IE5vbmU6CgogICAgICAgIHByaW50KHNlbGYuZGlzcGxheV9iYW5uZXIoKSkKCiAgICAgICAgd2hpbGUgVHJ1ZToKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgc2xlZXAoMSkKICAgICAgICAgICAgICAgIHZpZXdzLCBzaGFyZXMsIGxpa2VzLCBjb21tZW50cywgc2F2ZXMgPSBzZWxmLmdldF9zdGF0cyh2aWRlb19pZCkKICAgICAgICAgICAgICAgIHNlbGYuX3ByaW50KCfinpUnLCBmJ1N0YXRzOiBbVmlld3M6IHt2aWV3c30gfCBTaGFyZXM6IHtzaGFyZXN9IHwgTGlrZXM6IHtsaWtlc30gfCBDb21tZW50czoge2NvbW1lbnRzfSB8IFNhdmVzOiB7c2F2ZXN9XScsIG5ld19saW5lPUZhbHNlKQogICAgICAgICAgICBleGNlcHQ6IGNvbnRpbnVlCgogICAgZGVmIGdldF9pZChzZWxmLCB2aWRlb191cmw6IHN0cikgLT4gc3RyOgogICAgICAgIHJldHVybiB2aWRlb191cmwuc3BsaXQoJz8nKVswXS5zcGxpdCgnLycpWy0xXQoKICAgIGRlZiB3YWl0X2Zvcl9wYXRoKHNlbGYsIHhwYXRoOiBzdHIpIC0+IFdlYkVsZW1lbnQ6CiAgICAgICAgd2hpbGUgVHJ1ZToKICAgICAgICAgICAgdHJ5OiByZXR1cm4gc2VsZi5kcml2ZXIuZmluZF9lbGVtZW50KEJ5LlhQQVRILCB4cGF0aCkKICAgICAgICAgICAgZXhjZXB0OiBjb250aW51ZQoKICAgIGRlZiBsb2FkX3plZm95KHNlbGYpIC0+IE5vbmU6CiAgICAgICAgc2VsZi5kcml2ZXIgPSBzZWxmLnNldHVwX2RyaXZlcigpCiAgICAgICAgc2VsZi5kcml2ZXIuc2V0X3dpbmRvd19zaXplKDYwMCwgOTAwKQogICAgICAgIHNsZWVwKDIpCgogICAgICAgIHNlbGYuZHJpdmVyLmV4ZWN1dGVfc2NyaXB0KCd3aW5kb3cub3BlbigiaHR0cHM6Ly96ZWZveS5jb20iKTsnKQogICAgICAgICNzZWxmLmRyaXZlci5nZXQoJ2h0dHBzOi8vemVmb3kuY29tJykKICAgICAgICAKICAgICAgICByZXMgPSAnJwoKICAgICAgICB3aGlsZSBub3QgJ0VudGVyIHRoZSB3b3JkJyBpbiByZXM6CiAgICAgICAgICAgIHdpdGggQnl0ZXNJTygpIGFzIGJ5dGVzX2FycmF5OgogICAgICAgICAgICAgICAgSW1hZ2VHcmFiLmdyYWIoKS5zYXZlKGJ5dGVzX2FycmF5LCBmb3JtYXQ9J1BORycpCiAgICAgICAgICAgICAgICByZXMgPSBwb3N0KCdodHRwczovL3BsYXRpcHVzOTk5OS5weXRob25hbnl3aGVyZS5jb20nLCBqc29uPXsnaW1hZ2UnOiBiNjRlbmNvZGUoYnl0ZXNfYXJyYXkuZ2V0dmFsdWUoKSkuZGVjb2RlKCl9KS50ZXh0CgoKICAgICAgICBzZWxmLmRyaXZlci5jbG9zZSgpCiAgICAgICAgc2VsZi5kcml2ZXIuc3dpdGNoX3RvLndpbmRvdyhzZWxmLmRyaXZlci53aW5kb3dfaGFuZGxlc1swXSkKICAgIAogICAgZGVmIHNvbHZlKHNlbGYpIC0+IE5vbmU6CiAgICAgICAgaW1hZ2VfeHBhdGggPSBzZWxmLmNhcHRjaGFfYm94ICsgJy9pbWcnCgogICAgICAgIGZhaWxlZCA9IEZhbHNlCgogICAgICAgIHdoaWxlIFRydWU6CiAgICAgICAgICAgIGlmIGZhaWxlZDoKICAgICAgICAgICAgICAgIGltYWdlX3hwYXRoLCBzZWxmLmNhcHRjaGFfcmVzLCBzZWxmLmNhcHRjaGFfYnV0dG9uID0gZiJ7aW1hZ2VfeHBhdGh9OntzZWxmLmNhcHRjaGFfcmVzfTp7c2VsZi5jYXB0Y2hhX2J1dHRvbn0iLnJlcGxhY2UoJzUnLCAnNicpLnNwbGl0KCc6JykKCiAgICAgICAgICAgIGltZyA9IHNlbGYud2FpdF9mb3JfcGF0aChpbWFnZV94cGF0aCkuc2NyZWVuc2hvdF9hc19iYXNlNjQKCiAgICAgICAgICAgIGNhcHRjaGFfYW5zd2VyID0gcG9zdCgnaHR0cHM6Ly9wbGF0aXB1czk5OTkucHl0aG9uYW55d2hlcmUuY29tJywganNvbj17J2ltYWdlJzogaW1nfSkudGV4dC5zcGxpdCgnXG4nKVswXQoKICAgICAgICAgICAgc2VsZi5fcHJpbnQoJyEnLCBmJ3tjYXB0Y2hhX2Fuc3dlcn0nKQoKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgaWYgbm90IERpY3QoImVuX1VTIikuY2hlY2soY2FwdGNoYV9hbnN3ZXIpOgogICAgICAgICAgICAgICAgICAgIGNhcHRjaGFfYW5zd2VyID0gRGljdCgiZW5fVVMiKS5zdWdnZXN0KGNhcHRjaGFfYW5zd2VyKVswXQogICAgICAgICAgICAgICAgICAgIHNlbGYuX3ByaW50KCchJywgZidUcnlpbmcge2NhcHRjaGFfYW5zd2VyfScpCiAgICAgICAgICAgIGV4Y2VwdDogcGFzcwoKICAgICAgICAgICAgc2VsZi5kcml2ZXIuZmluZF9lbGVtZW50KEJ5LlhQQVRILCBzZWxmLmNhcHRjaGFfcmVzKS5zZW5kX2tleXMoY2FwdGNoYV9hbnN3ZXIpCiAgICAgICAgICAgIHNlbGYuZHJpdmVyLmZpbmRfZWxlbWVudChCeS5YUEFUSCwgc2VsZi5jYXB0Y2hhX2J1dHRvbikuY2xpY2soKQoKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgc2xlZXAoMSkKICAgICAgICAgICAgICAgIHNlbGYuZHJpdmVyLmZpbmRfZWxlbWVudChCeS5YUEFUSCwgc2VsZi5wYXRoc1s0XVswXSkKICAgICAgICAgICAgICAgIGJyZWFrCgogICAgICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgICAgICBzZWxmLndhaXRfZm9yX3BhdGgoJy8vKltAaWQ9ImVycm9yY2FwdGhjYWNsb3NlIl0vZGl2L2Rpdi9kaXZbM10vYnV0dG9uJykuY2xpY2soKQogICAgICAgICAgICAgICAgZmFpbGVkID0gVHJ1ZQoKICAgIGRlZiBjaG9pY2Vfc2VydmljZShzZWxmKSAtPiBOb25lOgoKICAgICAgICBkaXNwbGF5X2RpY3QgPSB7CiAgICAgICAgICAgIFRydWUgIDogJ+KchScsCiAgICAgICAgICAgIEZhbHNlIDogJ+KdjCcKICAgICAgICB9CgogICAgICAgIHByaW50KHNlbGYuZGlzcGxheV9iYW5uZXIoKSkKCiAgICAgICAgZm9yIG51bWJlciwgeHBhdGggaW4gc2VsZi5wYXRocy5pdGVtcygpOgogICAgICAgICAgICBpc19lbmFibGVkID0gc2VsZi5kcml2ZXIuZmluZF9lbGVtZW50KEJ5LlhQQVRILCB4cGF0aFswXSkuaXNfZW5hYmxlZCgpCiAgICAgICAgICAgIG5hbWUgICA9IHNlbGYuZHJpdmVyLmZpbmRfZWxlbWVudChCeS5YUEFUSCwgeHBhdGhbMF0ucmVwbGFjZSgnYnV0dG9uJywgJ2g1JykpLnRleHQKICAgICAgICAgICAgCiAgICAgICAgICAgIHNlbGYuX3ByaW50KG51bWJlciwgZid7bmFtZX17IiAiICogKGxlbigiQ29tbWVudHMgSGVhcnRzICIpIC0gbGVuKG5hbWUpKX0gfCBTdGF0dXM6IHtkaXNwbGF5X2RpY3RbaXNfZW5hYmxlZF19JykKCiAgICAgICAgcHJpbnQoKQogICAgICAgIHNlbGYuY2hvaWNlID0gaW50KGlucHV0KHNlbGYuX3ByaW50KCc/JywgJ0Nob2ljZSBhIHNlcnZpY2UgPiAnLCBpbnB1dD1UcnVlKSkpCgogICAgZGVmIHdhaXQoc2VsZiwgc2Vjb25kczogaW50KSAtPiBOb25lOgogICAgICAgIGZvciBzZWNvbmQgaW4gcmFuZ2Uoc2Vjb25kcyk6CiAgICAgICAgICAgIHNlbGYudGl0bGUoZidaZWZveS1ib3QgejhsYyDilo8gIFNlbnQ6IHtzZWxmLnNlbnR9IOKWjyAgQ29vbGRvd246IHtzZWNvbmRzIC0gKHNlY29uZCArIDEpfScpCiAgICAgICAgICAgIHNsZWVwKDEpCgogICAgZGVmIHRhc2soc2VsZikgLT4gTm9uZToKICAgICAgICBzZWxmLmRyaXZlci5maW5kX2VsZW1lbnQoQnkuWFBBVEgsIHNlbGYuc2VhcmNoX2JveC5yZXBsYWNlKCctJywgZid7c2VsZi5kaXZ9JykpLmNsaWNrKCkKICAgICAgICBzbGVlcCgzKQogICAgICAgICAgICAKICAgICAgICBzZWNvbmRzID0gc2VsZi5jaGVja19zdWJtaXQoKQogICAgICAgIGlmIHR5cGUoc2Vjb25kcykgPT0gaW50OgogICAgICAgICAgICBzZWxmLndhaXQoc2Vjb25kcykKICAgICAgICAgICAgc2xlZXAoMikKICAgICAgICAgICAgc2VsZi5kcml2ZXIuZmluZF9lbGVtZW50KEJ5LlhQQVRILCBzZWxmLnNlYXJjaF9ib3gucmVwbGFjZSgnLScsIGYne3NlbGYuZGl2fScpKQogICAgICAgICAgICAKICAgICAgICBzbGVlcCgyKQoKICAgICAgICB3aGlsZSBUcnVlOgogICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICBzZWxmLmRyaXZlci5leGVjdXRlX3NjcmlwdCgiZnVuY3Rpb24gZmluZF9lbGVtZW50KHBhdGgpIHtyZXR1cm4gZG9jdW1lbnQuZXZhbHVhdGUocGF0aCwgZG9jdW1lbnQsIG51bGwsIFhQYXRoUmVzdWx0LkZJUlNUX09SREVSRURfTk9ERV9UWVBFLCBudWxsKS5zaW5nbGVOb2RlVmFsdWU7IH0gZmluZF9lbGVtZW50KCciICsgZicvLypbQGlkPSJ7c2VsZi5wYXRoc1tzZWxmLmNob2ljZV1bMV19Il0vZGl2WzFdL2Rpdi9mb3JtL2J1dHRvbicgKyAiJykuY2xpY2soKTsiKQogICAgICAgICAgICAgICAgYnJlYWsKICAgICAgICAgICAgZXhjZXB0OgogICAgICAgICAgICAgICAgc2VsZi5kcml2ZXIuZmluZF9lbGVtZW50KEJ5LlhQQVRILCBzZWxmLnNlYXJjaF9ib3gucmVwbGFjZSgnLScsIGYne3NlbGYuZGl2fScpKS5jbGljaygpCgogICAgICAgICAgICBzbGVlcCgyKQoKCiAgICAgICAgd2hpbGUgVHJ1ZToKICAgICAgICAgICAgc291cmNlID0gc2VsZi5kcml2ZXIucGFnZV9zb3VyY2UKCiAgICAgICAgICAgIGlmICdzZW50JyBpbiBzb3VyY2U6CiAgICAgICAgICAgICAgICBzZWxmLnNlbnQgKz0gMQogICAgICAgICAgICAgICAgc2VsZi50aXRsZShmJ1plZm95IEJvdCB6OGxjIOKWjyAgU2VudDoge3NlbGYuc2VudH0g4paPICBDb29sZG93bjogMCcpCiAgICAgICAgICAgICAgICBicmVhawogICAgICAgICAgICAKICAgICAgICAgICAgaWYgJ1RvbyBtYW55IHJlcXVlc3RzJyBpbiBzb3VyY2U6CiAgICAgICAgICAgICAgICBzbGVlcCgzKQogICAgICAgICAgICAgICAgYnJlYWsKICAgICAgICAgICAgCgoKICAgIGRlZiBjaGVja19zdWJtaXQoc2VsZik6CiAgICAgICAgdHJ5OgogICAgICAgICAgICB0aW1lcl9yZXNwb25zZSA9IHNlbGYuZHJpdmVyLmZpbmRfZWxlbWVudChCeS5YUEFUSCwgZicvLypbQGlkPSJ7c2VsZi5wYXRoc1tzZWxmLmNob2ljZV1bMV19Il0vc3BhbicpLnRleHQKCiAgICAgICAgICAgIGlmICdSRUFEWScgaW4gIHRpbWVyX3Jlc3BvbnNlOgogICAgICAgICAgICAgICAgcmV0dXJuIFRydWUKICAgICAgICAgICAgCiAgICAgICAgICAgIGVsaWYgInNlY29uZHMgZm9yIHlvdXIgbmV4dCBzdWJtaXQiIGluICB0aW1lcl9yZXNwb25zZToKICAgICAgICAgICAgICAgIG1pbnV0ZXMsIHNlY29uZHMgPSBmaW5kYWxsKHInXGQrJywgIHRpbWVyX3Jlc3BvbnNlKQogICAgICAgICAgICAgICAgcmV0dXJuIHNlbGYuY29udmVydChpbnQobWludXRlcyksIGludChzZWNvbmRzKSkKCiAgICAgICAgZXhjZXB0OgogICAgICAgICAgICByZXR1cm4gRmFsc2UKICAgICAgICAgICAgCiAgICBkZWYgbWFpbihzZWxmKSAtPiBOb25lOgogICAgICAgIHNlbGYuY2xlYXIoKQogICAgICAgIHByaW50KHNlbGYuZGlzcGxheV9iYW5uZXIoKSkKICAgICAgICBzZWxmLnRpdGxlKCdaZWZveSBCb3QgejhsYyDilo8gIFN0YXR1czogTG9hZGluZycpCgogICAgICAgIHZpZGVvX3VybCA9IGlucHV0KHNlbGYuX3ByaW50KCc/JywgJ1ZpZGVvIFVybCA+ICcsIGlucHV0PVRydWUpKQogICAgICAgIHZpZGVvX2lkID0gc2VsZi5nZXRfaWQodmlkZW9fdXJsKQoKICAgICAgICBzZWxmLl9wcmludCgnIScsICdCcm93c2VyIGlzIGxvYWRpbmdcbicpCiAgICAgICAgc2VsZi5sb2FkX3plZm95KCkKICAgICAgICBzZWxmLndhaXRfZm9yX3BhdGgoc2VsZi5jYXB0Y2hhX2JveCkKCiAgICAgICAgc2VsZi50aXRsZSgnWmVmb3kgQm90IHo4bGMg4paPICBTdGF0dXM6IFNvbHZpbmcnKQogICAgICAgIHNlbGYuX3ByaW50KCcqJywgJ1NvbHZpbmcgVGhlIENhcHRjaGEnKQogICAgICAgIHNlbGYuc29sdmUoKQogICAgICAgIAogICAgICAgIHNlbGYuY2xlYXIoKQogICAgICAgIHNlbGYudGl0bGUoJ1plZm95IEJvdCB6OGxjIOKWjyAgU3RhdHVzOiBOL0EnKQoKICAgICAgICBzZWxmLmNob2ljZV9zZXJ2aWNlKCkKCiAgICAgICAgc2VsZi5kcml2ZXIuZmluZF9lbGVtZW50KEJ5LlhQQVRILCBzZWxmLnBhdGhzW3NlbGYuY2hvaWNlXVswXSkuY2xpY2soKQoKICAgICAgICBzZWxmLmRpdiA9IGludChmaW5kYWxsKHInXGQrJywgc2VsZi5wYXRoc1tzZWxmLmNob2ljZV1bMF0pWy0xXSkgKyA1CgogICAgICAgIHNlbGYuY2xlYXIoKQogICAgICAgIFRocmVhZCh0YXJnZXQgPSBzZWxmLmRpc3BsYXlfc3RhdHMsIGFyZ3MgPSBbdmlkZW9faWQsXSkuc3RhcnQoKQoKICAgICAgICBzZWxmLmRyaXZlci5maW5kX2VsZW1lbnQoQnkuWFBBVEgsIHNlbGYudmlkZW9fdXJsX2JveC5yZXBsYWNlKCctJywgZid7c2VsZi5kaXZ9JykpLnNlbmRfa2V5cyh2aWRlb191cmwpCgogICAgICAgIHdoaWxlIFRydWU6CiAgICAgICAgICAgIHNlbGYudGFzaygpCiAgICAgICAgCgppZiBfX25hbWVfXyA9PSAnX19tYWluX18nOgogICAgWmVmb3koKS5tYWluKCk=')
encoded

data = base64.b64decode(encoded)
data
