import os
import sys
import subprocess

if sys.argv[2] == 'run_in_child':
    print("CHILD")
    subprocess.run(
        [
            os.path.basename(sys.executable),
            '-m',
            'mess',
            sys.argv[1],
            '--child'
        ]
    )

if sys.argv[2] != '--child':
    print("PARENT")
def entrypoint():
    with open(sys.argv[1], "rb") as prog_being_profiled:
        program_path = os.path.dirname(os.path.abspath(sys.argv[1]))
        code = compile(prog_being_profiled.read(), sys.argv[1], "exec")
        sys.path.insert(0, program_path)
        # Grab local and global variables.
        import __main__
        the_locals = __main__.__dict__
        the_globals = __main__.__dict__
        print(the_globals)
        # Splice in the name of the file being executed instead of the profiler.
        print("MAIN ", __main__)
        the_globals["__file__"] = os.path.basename(sys.argv[1])
        the_globals["__spec__"] = None
        try:

            exec(code, the_globals, the_locals)
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':

    entrypoint()
