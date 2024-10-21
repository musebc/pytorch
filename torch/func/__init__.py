from torch._functorch.apis import grad, grad_and_value, vmap
from torch._functorch.batch_norm_replacement import replace_all_batch_norm_modules_
from torch._functorch.eager_transforms import (
    functionalize,
    hessian,
    jacfwd,
    jacrev,
    jvp,
    linearize,
    vjp,
)
from torch._functorch.functional_call import functional_call, stack_module_state
