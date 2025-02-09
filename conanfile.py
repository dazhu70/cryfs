from conan import ConanFile

class CryFSConan(ConanFile):
	settings = "os", "compiler", "build_type", "arch"
	requires = [
		"range-v3/0.12.0",
		"spdlog/1.11.0",
		"boost/1.79.0",
	]
	generators = "cmake"
	default_options = {
		"boost/*:system_no_deprecated": True,
		"boost/*:asio_no_deprecated": True,
		"boost/*:filesystem_no_deprecated": True,
		"boost/*:without_atomic": False,  # needed by boost thread
		"boost/*:without_chrono": False,  # needed by CryFS
		"boost/*:without_container": False,  # needed by boost thread
		"boost/*:without_context": True,
		"boost/*:without_contract": True,
		"boost/*:without_coroutine": True,
		"boost/*:without_date_time": False,  # needed by boost thread
		"boost/*:without_exception": False,  # needed by boost thread
		"boost/*:without_fiber": True,
		"boost/*:without_filesystem": False,  # needed by CryFS
		"boost/*:without_graph": True,
		"boost/*:without_graph_parallel": True,
		"boost/*:without_iostreams": True,
		"boost/*:without_json": True,
		"boost/*:without_locale": True,
		"boost/*:without_log": True,
		"boost/*:without_math": True,
		"boost/*:without_mpi": True,
		"boost/*:without_nowide": True,
		"boost/*:without_program_options": False,  # needed by CryFS
		"boost/*:without_python": True,
		"boost/*:without_random": True,
		"boost/*:without_regex": True,
		"boost/*:without_serialization": False,  # needed by boost date_time
		# Stacktrace is needed by CryFS. Stacktrace is a header-only library and linking against its static version actually **disables** stacktraces,
		# see https://www.boost.org/doc/libs/1_65_0/doc/html/stacktrace/getting_started.html#stacktrace.getting_started.enabling_and_disabling_stacktrac
		# This is why we need to **not** link against the static version of stacktrace.
		"boost/*:without_stacktrace": True,
		"boost/*:without_system": False,  # needed by CryFS
		"boost/*:without_test": True,
		"boost/*:without_thread": False,  # needed by CryFS
		"boost/*:without_timer": True,
		"boost/*:without_type_erasure": True,
		"boost/*:without_wave": True,
	}
