from autodiff.symbolic import Function, Gradient, HessianVector


def function(fn=None, **kwargs):
    """
    Wraps a function with an AutoDiff Function instance, converting it to a
    symbolic representation.

    The function is compiled the first time it is called.

    Use:
        @function
        def python_function(...):
            return do_something()

        python_function(...) # calls compiled Function

    Pass keywords to Function:

        @function(force_floatX=True):
            def python_function(x=1, y=2):
                return do_something()
    """
    if callable(fn):
        return Function(fn, **kwargs)
    else:
        def function_wrapper(pyfn):
            return Function(pyfn, **kwargs)
        return function_wrapper


def gradient(fn=None, **kwargs):
    """
    Wraps a function with an AutoDiff Gradient instance, converting it to a
    symbolic representation that returns the derivative with respect to either
    all inputs or a subset (if specified with the 'wrt' keyword).

    The function is compiled the first time it is called.
    Use:

        @gradient
        def python_function(...):
            return do_something()

        python_function(...) # returns the gradient of python_function

    Pass keywords to Gradient:

        @gradient(wrt = ['x', 'y'])
        def python_function(x=1, y=2):
            return do_something()

    """
    if callable(fn):
        return Gradient(fn, **kwargs)
    else:
        def gradient_wrapper(pyfn):
            return Gradient(pyfn, **kwargs)
        return gradient_wrapper


def hessian_vector(fn=None, **kwargs):
    """
    Wraps a function with an AutoDiff HessianVector instance, converting it to
    a symbolic representation that returns the result with respect to either
    all inputs or a subset (if specified with the 'wrt' keyword). A tuple of
    the required vectors must be passed to the resulting function with the
    keyword '_vectors'.

    The function is compiled the first time it is called.
    Use:

        @gradient
        def python_function(...):
            return do_something()

        python_function(...) # returns the gradient of python_function

    Pass keywords to Gradient:

        @gradient(wrt = ['x', 'y'])
        def python_function(x=1, y=2):
            return do_something()

    """
    if callable(fn):
        return HessianVector(fn, **kwargs)
    else:
        def hv_wrapper(pyfn):
            return HessianVector(pyfn, **kwargs)
        return hv_wrapper
